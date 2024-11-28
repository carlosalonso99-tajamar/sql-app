# README: Documentación de SQL para Examen

Este documento es una guía completa de los comandos de SQL más importantes, explicando su funcionamiento y proporcionando ejemplos sencillos para ayudar a prepararse para el examen. Contiene desde consultas básicas hasta funciones agregadas y uniones, cubriendo todo lo necesario para obtener una buena puntuación.

## Tabla de Contenidos
1. [Comandos Básicos de Selección](#1-comandos-básicos-de-selección)
   - 1.1 [`SELECT`](#11-select)
   - 1.2 [`WHERE`](#12-where)
   - 1.3 [`ORDER BY`](#13-order-by)
   - 1.4 [`LIMIT`](#14-limit)
2. [Filtrado y Condiciones](#2-filtrado-y-condiciones)
   - 2.1 [`LIKE` y `IN`](#21-like-e-in)
   - 2.2 [`BETWEEN`](#22-between)
   - 2.3 [`IS NULL` / `IS NOT NULL`](#23-is-null--is-not-null)
3. [Funciones Agregadas](#3-funciones-agregadas)
   - 3.1 [`COUNT()`](#31-count)
   - 3.2 [`SUM()` y `AVG()`](#32-sum-y-avg)
   - 3.3 [`MIN()` y `MAX()`](#33-min-y-max)
4. [Agrupaciones](#4-agrupaciones)
   - 4.1 [`GROUP BY`](#41-group-by)
   - 4.2 [`HAVING`](#42-having)
5. [Joins (Uniones)](#5-joins-uniones)
   - 5.1 [`INNER JOIN`](#51-inner-join)
   - 5.2 [`LEFT JOIN`](#52-left-join)
   - 5.3 [`RIGHT JOIN`](#53-right-join)
   - 5.4 [`FULL OUTER JOIN`](#54-full-outer-join)
6. [Operaciones sobre Tablas](#6-operaciones-sobre-tablas)
   - 6.1 [`CREATE TABLE`](#61-create-table)
   - 6.2 [`INSERT INTO`](#62-insert-into)
   - 6.3 [`UPDATE`](#63-update)
   - 6.4 [`DELETE`](#64-delete)
7. [Consultas Complejas](#7-consultas-complejas)
   - 7.1 [Subconsultas](#71-subconsultas)
   - 7.2 [Funciones de Ventana](#72-funciones-de-ventana)
8. [Operadores de Unión y Set](#8-operadores-de-unión-y-set)
   - 8.1 [`UNION` y `UNION ALL`](#81-union-y-union-all)
9. [Índices](#9-índices)
   - 9.1 [`CREATE INDEX`](#91-create-index)
10. [Cláusula `DISTINCT`](#10-cláusula-distinct)
11. [Operaciones de Fecha y Hora](#11-operaciones-de-fecha-y-hora)
   - 11.1 [Funciones de Fecha](#111-funciones-de-fecha)
12. [Transacciones](#12-transacciones)
   - 12.1 [`BEGIN`, `COMMIT`, `ROLLBACK`](#121-begin-commit-rollback)
13. [Cláusula `CASE`](#13-cláusula-case)
14. [Funciones de Texto](#14-funciones-de-texto)
15. [Conclusión](#15-conclusión)

## 1. Comandos Básicos de Selección

### 1.1 `SELECT`
El comando `SELECT` se usa para recuperar datos de una o más tablas.
```sql
SELECT columna1, columna2
FROM tabla;
```
**Ejemplo**: Seleccionar los nombres y edades de una tabla de empleados.
```sql
SELECT nombre, edad
FROM empleados;
```

### 1.2 `WHERE`
Filtra las filas según una condición especificada.
```sql
SELECT *
FROM empleados
WHERE edad > 30;
```

### 1.3 `ORDER BY`
Ordena los resultados por una o varias columnas.
```sql
SELECT *
FROM empleados
ORDER BY salario DESC;
```
**Ejemplo**: Ordenar a los empleados por edad en orden ascendente.

### 1.4 `LIMIT`
Restringe el número de filas devueltas por la consulta.
```sql
SELECT *
FROM empleados
LIMIT 5;
```

## 2. Filtrado y Condiciones

### 2.1 `LIKE` e `IN`
- **`LIKE`** se usa para buscar un patrón en una columna.
- **`IN`** se usa para filtrar filas que coincidan con uno de varios valores.
```sql
SELECT *
FROM empleados
WHERE nombre LIKE 'A%';  -- Nombres que empiezan con 'A'

SELECT *
FROM empleados
WHERE departamento IN ('Ventas', 'IT');
```

### 2.2 `BETWEEN`
Filtra filas cuyos valores se encuentren dentro de un rango especificado.
```sql
SELECT *
FROM empleados
WHERE edad BETWEEN 25 AND 35;
```

### 2.3 `IS NULL` / `IS NOT NULL`
Comprueba si una columna tiene o no un valor nulo.
```sql
SELECT *
FROM empleados
WHERE telefono IS NULL;
```

## 3. Funciones Agregadas

### 3.1 `COUNT()`
Cuenta el número de filas que cumplen una condición.
```sql
SELECT COUNT(*)
FROM empleados;
```

### 3.2 `SUM()` y `AVG()`
- **`SUM()`** calcula la suma total de una columna.
- **`AVG()`** calcula el promedio de una columna.
```sql
SELECT SUM(salario) AS TotalSalarios
FROM empleados;

SELECT AVG(edad) AS EdadPromedio
FROM empleados;
```

### 3.3 `MIN()` y `MAX()`
Encuentran el valor mínimo y máximo de una columna.
```sql
SELECT MIN(salario) AS SalarioMinimo, MAX(salario) AS SalarioMaximo
FROM empleados;
```

## 4. Agrupaciones

### 4.1 `GROUP BY`
Agrupa filas que tienen los mismos valores en columnas específicas.
```sql
SELECT departamento, COUNT(*) AS NumeroEmpleados
FROM empleados
GROUP BY departamento;
```

### 4.2 `HAVING`
Filtra grupos después de aplicar `GROUP BY`.
```sql
SELECT departamento, AVG(salario) AS SalarioPromedio
FROM empleados
GROUP BY departamento
HAVING AVG(salario) > 50000;
```

## 5. Joins (Uniones)

### 5.1 `INNER JOIN`
Devuelve filas que tienen coincidencias en ambas tablas.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
INNER JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

### 5.2 `LEFT JOIN`
Devuelve todas las filas de la tabla izquierda y las coincidencias de la tabla derecha. Si no hay coincidencia, los valores de la tabla derecha serán nulos.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
LEFT JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

### 5.3 `RIGHT JOIN`
Devuelve todas las filas de la tabla derecha y las coincidencias de la tabla izquierda. Si no hay coincidencia, los valores de la tabla izquierda serán nulos.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
RIGHT JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

### 5.4 `FULL OUTER JOIN`
Devuelve todas las filas cuando hay una coincidencia en cualquiera de las tablas.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
FULL OUTER JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

## 6. Operaciones sobre Tablas

### 6.1 `CREATE TABLE`
Crea una nueva tabla en la base de datos.
```sql
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    salario DECIMAL(10, 2)
);
```

### 6.2 `INSERT INTO`
Inserta nuevos registros en una tabla.
```sql
INSERT INTO empleados (id, nombre, edad, salario)
VALUES (1, 'Juan', 28, 30000.00);
```

### 6.3 `UPDATE`
Actualiza registros existentes en una tabla.
```sql
UPDATE empleados
SET salario = salario * 1.1
WHERE departamento = 'IT';
```

### 6.4 `DELETE`
Elimina registros de una tabla.
```sql
DELETE FROM empleados
WHERE edad < 25;
```

## 7. Consultas Complejas

### 7.1 Subconsultas
Consultas anidadas dentro de otra consulta.
```sql
SELECT nombre
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);
```

### 7.2 Funciones de Ventana
Permiten realizar cálculos sobre un conjunto de filas relacionadas con la fila actual.
```sql
SELECT nombre, salario, RANK() OVER (ORDER BY salario DESC) AS ranking
FROM empleados;
```

## 8. Operadores de Unión y Set

### 8.1 `UNION` y `UNION ALL`
Para combinar los resultados de dos o más consultas.
```sql
SELECT nombre FROM empleados WHERE departamento = 'IT'
UNION
SELECT nombre FROM empleados WHERE salario > 50000;
```

## 9. Índices

### 9.1 `CREATE INDEX`
Ayuda a acelerar las consultas creando índices sobre columnas.
```sql
CREATE INDEX idx_nombre ON empleados(nombre);
```

## 10. Cláusula `DISTINCT`
Retorna solo valores distintos en los resultados.
```sql
SELECT DISTINCT departamento FROM empleados;
```

## 11. Operaciones de Fecha y Hora

### 11.1 Funciones de Fecha
Funciones comunes para manejar y comparar fechas, como `DATE()`, `NOW()`, `DATEDIFF()`.
```sql
SELECT nombre FROM empleados WHERE DATE(contratacion) = '2023-01-01';
```

## 12. Transacciones

### 12.1 `BEGIN`, `COMMIT`, `ROLLBACK`
Para agrupar una serie de operaciones y asegurar la integridad de los datos.
```sql
BEGIN;
UPDATE empleados SET salario = salario * 1.05 WHERE departamento = 'Ventas';
DELETE FROM empleados WHERE edad < 25;
COMMIT;
```

## 13. Cláusula `CASE`
Para generar resultados personalizados según condiciones específicas.
```sql
SELECT nombre,
       CASE 
         WHEN salario > 50000 THEN 'Alto'
         WHEN salario BETWEEN 30000 AND 50000 THEN 'Medio'
         ELSE 'Bajo'
       END AS nivel_salarial
FROM empleados;
```

## 14. Funciones de Texto
Funciones para manejar texto, como `CONCAT()`, `UPPER()`, `LOWER()`, `TRIM()`.
```sql
SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM empleados;
```

## 15. Conclusión

Esta guía cubre los comandos esenciales de SQL para prepararte para el examen. Practica estos ejemplos y asegúrate de comprender cómo y cuándo usar cada uno de ellos. Con un buen dominio de estos conceptos, estarás listo para manejar cualquier consulta que se presente durante el examen.
