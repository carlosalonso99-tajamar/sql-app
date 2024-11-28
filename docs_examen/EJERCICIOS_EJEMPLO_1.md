# README: Ejercicios de Práctica para Examen de SQL

Este documento contiene ejemplos de ejercicios de SQL para practicar antes del examen. Estos ejercicios están diseñados para ayudarte a reforzar conceptos avanzados de consultas en SQL, incluyendo funciones agregadas, joins, subconsultas y agrupaciones, especialmente en el contexto de Hive y clústeres de Azure.

## Ejercicio 1: Retrasos de Vuelo
- **Instrucción**: Selecciona todos los registros del año 2023 donde el vuelo fue retrasado más de 60 minutos.
  - **Objetivo**: Practicar el filtrado de datos por condiciones específicas y seleccionar solo ciertas columnas.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT fecha, aerolinea, numero_vuelo, retraso_minutos
    FROM vuelos
    WHERE YEAR(fecha) = 2023 AND retraso_minutos > 60;
    ```

## Ejercicio 2: Promedio de Retrasos
- **Instrucción**: Calcula el promedio de retraso en la llegada y en la salida para cada aerolínea. Ordena los resultados en orden descendente por el retraso promedio en la llegada.
  - **Objetivo**: Practicar el uso de funciones agregadas y ordenación.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT aerolinea,
           AVG(retraso_llegada) AS retraso_promedio_llegada,
           AVG(retraso_salida) AS retraso_promedio_salida
    FROM vuelos
    GROUP BY aerolinea
    ORDER BY retraso_promedio_llegada DESC;
    ```

## Ejercicio 3: Rutas Más Comunes
- **Instrucción**: ¿Cuáles son las cinco rutas más comunes (aeropuerto de origen y destino) en los datos? Incluye el conteo de vuelos para cada ruta.
  - **Objetivo**: Practicar el uso de `GROUP BY`, contar registros y limitar el número de resultados.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT aeropuerto_origen, aeropuerto_destino, COUNT(*) AS total_vuelos
    FROM vuelos
    GROUP BY aeropuerto_origen, aeropuerto_destino
    ORDER BY total_vuelos DESC
    LIMIT 5;
    ```

## Ejercicio 4: Aeropuertos con Retrasos
- **Instrucción**: Encuentra los tres aeropuertos de destino con el mayor promedio de retraso en la llegada. Muestra el nombre del aeropuerto, el número total de vuelos y el retraso promedio.
  - **Objetivo**: Practicar agrupación, agregación y ordenación.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT aeropuerto_destino, COUNT(*) AS total_vuelos, AVG(retraso_llegada) AS retraso_promedio
    FROM vuelos
    GROUP BY aeropuerto_destino
    ORDER BY retraso_promedio DESC
    LIMIT 3;
    ```

## Ejercicio 5: Vuelos de Fines de Semana
- **Instrucción**: Selecciona todos los vuelos de los fines de semana (sábado y domingo) con origen en un aeropuerto específico y cuyo retraso en salida o llegada haya sido superior a 30 minutos.
  - **Objetivo**: Practicar el filtrado con condiciones múltiples.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT *
    FROM vuelos
    WHERE (DAYOFWEEK(fecha) = 7 OR DAYOFWEEK(fecha) = 1)
      AND aeropuerto_origen = 'JFK'
      AND (retraso_salida > 30 OR retraso_llegada > 30);
    ```

## Ejercicio 6: Promedio de Retraso Mensual
- **Instrucción**: Encuentra el promedio de retraso en los vuelos para cada mes y año. Crea una tabla con las columnas de año, mes y promedio de retraso en minutos.
  - **Objetivo**: Practicar agrupación y cálculos mensuales.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT YEAR(fecha) AS anio, MONTH(fecha) AS mes, AVG(retraso_minutos) AS retraso_promedio
    FROM vuelos
    GROUP BY YEAR(fecha), MONTH(fecha);
    ```

## Ejercicio 7: Resumen de Vuelos Retrasados
- **Instrucción**: Crea una tabla llamada `DelayedFlightsSummary` que contenga un resumen de los vuelos con retraso superior a 45 minutos en la llegada o salida.
  - **Objetivo**: Practicar la creación y llenado de una tabla basada en un conjunto de resultados.
  - **Consulta de Ejemplo**:
    ```sql
    CREATE TABLE DelayedFlightsSummary AS
    SELECT YEAR(fecha) AS anio, MONTH(fecha) AS mes, aerolinea, aeropuerto_origen, aeropuerto_destino,
           COUNT(*) AS total_vuelos_retrasados, AVG(retraso_minutos) AS retraso_promedio
    FROM vuelos
    WHERE retraso_llegada > 45 OR retraso_salida > 45
    GROUP BY YEAR(fecha), MONTH(fecha), aerolinea, aeropuerto_origen, aeropuerto_destino;
    ```

## Ejercicio 8: Vuelos por Duración
- **Instrucción**: Selecciona los vuelos con una duración (tiempo de vuelo) superior al promedio de duración de todos los vuelos en el mismo año.
  - **Objetivo**: Practicar subconsultas y comparación.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT aerolinea, aeropuerto_origen, aeropuerto_destino, duracion_vuelo
    FROM vuelos v
    WHERE duracion_vuelo > (
        SELECT AVG(duracion_vuelo)
        FROM vuelos
        WHERE YEAR(fecha) = YEAR(v.fecha)
    );
    ```

## Ejercicio 9: Porcentaje de Vuelos Retrasados
- **Instrucción**: Encuentra el porcentaje de vuelos de cada aerolínea que han tenido un retraso en la llegada superior a 30 minutos.
  - **Objetivo**: Practicar cálculos de porcentaje y uso de `COUNT()`.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT aerolinea,
           (COUNT(CASE WHEN retraso_llegada > 30 THEN 1 END) * 100.0 / COUNT(*)) AS porcentaje_retrasados
    FROM vuelos
    GROUP BY aerolinea;
    ```

## Ejercicio 10: Unir Tablas de Aeropuertos
- **Instrucción**: Si tuvieras una tabla adicional de aeropuertos con columnas como `airport_code` y `airport_name`, escribe una consulta para unir esta tabla con los datos de vuelos y obtener el nombre del aeropuerto de origen y de destino en cada vuelo.
  - **Objetivo**: Practicar el uso de `JOIN` para unir tablas con diferentes tipos de información.
  - **Consulta de Ejemplo**:
    ```sql
    SELECT v.*, a_origen.airport_name AS aeropuerto_origen_nombre, a_destino.airport_name AS aeropuerto_destino_nombre
    FROM vuelos v
    JOIN aeropuertos a_origen ON v.aeropuerto_origen = a_origen.airport_code
    JOIN aeropuertos a_destino ON v.aeropuerto_destino = a_destino.airport_code;
    ```

Estos ejercicios te permitirán poner en práctica una variedad de conceptos y técnicas de SQL, desde funciones agregadas hasta joins complejos, asegurándote de estar preparado para el examen. ¡Buena suerte! 🚀

