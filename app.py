from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Asegúrate de que exista el directorio de subida
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


# Plantilla HTML con CodeMirror y la opción para cargar CSV
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Consulta SQLite</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/theme/dracula.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/mode/sql/sql.min.js"></script>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        .CodeMirror {
            height: auto;
        }
    </style>
</head>
<body>
    <h2>Cargar un CSV</h2>
    <form action="{{ url_for('upload_csv') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".csv">
        <input type="submit" value="Cargar CSV">
    </form>

    <h2>Consulta la base de datos de vuelos</h2>
    <form method="post">
        <label for="query">Escribe tu consulta SQL:</label><br><br>
        <textarea id="query" name="query" rows="4" cols="50">{{ query }}</textarea><br><br>
        <input type="submit" value="Ejecutar">
    </form>
    <h2>Resultados:</h2>
    {% if results %}
        <table>
            <thead>
                <tr>
                    {% for header in headers %}
                        <th>{{ header }}</th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in results %}
                    <tr>
                        {% for item in row %}
                            <td>{{ item }}</td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>No se encontraron resultados o no se ha ejecutado una consulta.</p>
    {% endif %}
    <script>
        var editor = CodeMirror.fromTextArea(document.getElementById('query'), {
            mode: 'text/x-sql',
            theme: 'dracula',
            lineNumbers: true,
            matchBrackets: true,
            autoCloseBrackets: true,
        });
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    query = ""
    results = []
    headers = []

    if request.method == 'POST':
        query = request.form['query']

        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        try:
            # Ejecutar la consulta
            c.execute(query)
            results = c.fetchall()
            headers = [description[0] for description in c.description]
        except Exception as e:
            results = [["Error: " + str(e)]]
        finally:
            conn.close()

    return render_template_string(HTML_TEMPLATE, query=query, results=results, headers=headers)

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Guardar el archivo en el servidor
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Leer el CSV y cargarlo en SQLite
        df = pd.read_csv(file_path)

        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Crear la tabla dinámicamente según las columnas del CSV
        table_name = 'tabla'
        columns = ', '.join([f"{col} TEXT" for col in df.columns])
        c.execute(f"DROP TABLE IF EXISTS {table_name}")
        c.execute(f"CREATE TABLE {table_name} ({columns})")

        # Insertar los datos del CSV en la tabla
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Cerrar la conexión
        conn.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
