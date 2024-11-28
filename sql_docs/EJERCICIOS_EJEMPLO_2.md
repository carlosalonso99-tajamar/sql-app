# Simulacro de Examen de SQL

Este documento contiene un simulacro de examen para practicar consultas SQL basadas en una tabla con la siguiente estructura:

| Campo              | Descripción                                |
|--------------------|--------------------------------------------|
| `year`             | Año del vuelo                              |
| `month`            | Mes del vuelo                              |
| `day`              | Día del vuelo                              |
| `airline`          | Aerolínea responsable del vuelo            |
| `flight_number`    | Número de vuelo                            |
| `origin_airport`   | Aeropuerto de origen                       |
| `destination_airport` | Aeropuerto de destino                    |
| `departure_delay`  | Retraso en la salida (en minutos)          |
| `arrival_delay`    | Retraso en la llegada (en minutos)         |
| `flight_duration`  | Duración del vuelo (en minutos)            |

### Pregunta 1: Filtrado por Demoras
1. Escribe una consulta que devuelva todos los vuelos que tuvieron un retraso en la salida mayor a 30 minutos.
   ```sql
   SELECT * 
   FROM flights
   WHERE departure_delay > 30;
   ```

### Pregunta 2: Duración Promedio de Vuelos
2. Escribe una consulta que muestre la duración promedio de los vuelos de cada aerolínea.
   ```sql
   SELECT airline, AVG(flight_duration) AS avg_flight_duration
   FROM flights
   GROUP BY airline;
   ```

### Pregunta 3: Origen y Destino Comunes
3. Escribe una consulta para encontrar los aeropuertos de origen y destino más comunes.
   ```sql
   SELECT origin_airport, destination_airport, COUNT(*) AS num_flights
   FROM flights
   GROUP BY origin_airport, destination_airport
   ORDER BY num_flights DESC
   LIMIT 5;
   ```

### Pregunta 4: Vuelos Sin Retraso
4. Escribe una consulta que devuelva los vuelos que no tuvieron retraso ni en la salida ni en la llegada.
   ```sql
   SELECT * 
   FROM flights
   WHERE departure_delay = 0 AND arrival_delay = 0;
   ```

### Pregunta 5: Retraso Total
5. Crea una nueva columna llamada `total_delay` que sume el retraso de salida y llegada. Muestra los primeros 10 registros ordenados por `total_delay` en orden descendente.
   ```sql
   SELECT *, (departure_delay + arrival_delay) AS total_delay
   FROM flights
   ORDER BY total_delay DESC
   LIMIT 10;
   ```

### Pregunta 6: Vuelos por Mes
6. Muestra cuántos vuelos hubo en cada mes.
   ```sql
   SELECT month, COUNT(*) AS total_flights
   FROM flights
   GROUP BY month
   ORDER BY month;
   ```

### Pregunta 7: Duración Máxima por Aerolínea
7. Encuentra el vuelo con la duración más larga para cada aerolínea.
   ```sql
   SELECT airline, MAX(flight_duration) AS longest_flight
   FROM flights
   GROUP BY airline;
   ```

### Pregunta 8: Salidas Retrasadas desde un Aeropuerto
8. Devuelve los vuelos que salieron con un retraso superior a 1 hora desde el aeropuerto "JFK".
   ```sql
   SELECT *
   FROM flights
   WHERE origin_airport = 'JFK' AND departure_delay > 60;
   ```

### Pregunta 9: Diferencia de Retrasos
9. Calcula la diferencia promedio entre el retraso de salida y el de llegada para todos los vuelos.
   ```sql
   SELECT AVG(departure_delay - arrival_delay) AS avg_delay_difference
   FROM flights;
   ```

### Pregunta 10: Cantidad de Vuelos entre Origen y Destino
10. Escribe una consulta que devuelva cuántos vuelos hubo entre cada par de aeropuertos (origen y destino).
    ```sql
    SELECT origin_airport, destination_airport, COUNT(*) AS flight_count
    FROM flights
    GROUP BY origin_airport, destination_airport;
    ```

---

Estas preguntas cubren varios aspectos de SQL, como filtrado, agregación, cálculos, y agrupamiento. Si necesitas más preguntas o quieres centrarte en un área específica, no dudes en pedírmelo.
