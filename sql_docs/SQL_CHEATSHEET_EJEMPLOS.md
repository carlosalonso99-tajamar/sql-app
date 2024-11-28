# Documentación Complementaria de SQL para Examen

Esta documentación complementaria contiene ejemplos prácticos detallados para cada uno de los apartados de la guía principal de SQL. Está diseñada para ayudar a entender mejor el uso de cada comando o función mediante ejemplos aplicados.

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
**Ejemplo**: Seleccionar todas las columnas de la tabla `empleados`.
```sql
SELECT *
FROM empleados;
```

**Ejemplo**: Seleccionar las columnas `nombre` y `edad` de la tabla `empleados`.
```sql
SELECT nombre, edad
FROM empleados;
```

### 1.2 `WHERE`
**Ejemplo**: Seleccionar los empleados cuya edad sea mayor a 30.
```sql
SELECT *
FROM empleados
WHERE edad > 30;
```

### 1.3 `ORDER BY`
**Ejemplo**: Seleccionar todos los empleados y ordenarlos por `salario` en orden descendente.
```sql
SELECT *
FROM empleados
ORDER BY salario DESC;
```

**Ejemplo**: Ordenar a los empleados por `edad` en orden ascendente.
```sql
SELECT *
FROM empleados
ORDER BY edad ASC;
```

### 1.4 `LIMIT`
**Ejemplo**: Seleccionar los primeros 5 empleados de la tabla.
```sql
SELECT *
FROM empleados
LIMIT 5;
```

## 2. Filtrado y Condiciones

### 2.1 `LIKE` e `IN`
**Ejemplo**: Seleccionar empleados cuyos nombres empiecen con la letra 'A'.
```sql
SELECT *
FROM empleados
WHERE nombre LIKE 'A%';
```

**Ejemplo**: Seleccionar empleados que pertenezcan a los departamentos 'Ventas' o 'IT'.
```sql
SELECT *
FROM empleados
WHERE departamento IN ('Ventas', 'IT');
```

### 2.2 `BETWEEN`
**Ejemplo**: Seleccionar empleados cuya edad esté entre 25 y 35 años.
```sql
SELECT *
FROM empleados
WHERE edad BETWEEN 25 AND 35;
```

### 2.3 `IS NULL` / `IS NOT NULL`
**Ejemplo**: Seleccionar empleados que no tengan registrado un número de teléfono.
```sql
SELECT *
FROM empleados
WHERE telefono IS NULL;
```

**Ejemplo**: Seleccionar empleados que tengan registrado un número de teléfono.
```sql
SELECT *
FROM empleados
WHERE telefono IS NOT NULL;
```

## 3. Funciones Agregadas

### 3.1 `COUNT()`
**Ejemplo**: Contar el número total de empleados.
```sql
SELECT COUNT(*)
FROM empleados;
```

### 3.2 `SUM()` y `AVG()`
**Ejemplo**: Calcular la suma total de los salarios de todos los empleados.
```sql
SELECT SUM(salario) AS TotalSalarios
FROM empleados;
```

**Ejemplo**: Calcular la edad promedio de los empleados.
```sql
SELECT AVG(edad) AS EdadPromedio
FROM empleados;
```

### 3.3 `MIN()` y `MAX()`
**Ejemplo**: Encontrar el salario más bajo y el más alto entre los empleados.
```sql
SELECT MIN(salario) AS SalarioMinimo, MAX(salario) AS SalarioMaximo
FROM empleados;
```

## 4. Agrupaciones

### 4.1 `GROUP BY`
**Ejemplo**: Contar el número de empleados en cada departamento.
```sql
SELECT departamento, COUNT(*) AS NumeroEmpleados
FROM empleados
GROUP BY departamento;
```

### 4.2 `HAVING`
**Ejemplo**: Mostrar los departamentos cuyo salario promedio sea mayor a 50,000.
```sql
SELECT departamento, AVG(salario) AS SalarioPromedio
FROM empleados
GROUP BY departamento
HAVING AVG(salario) > 50000;
```

## 5. Joins (Uniones)

### 5.1 `INNER JOIN`
**Ejemplo**: Seleccionar el nombre de los empleados y el nombre de sus departamentos.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
INNER JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

### 5.2 `LEFT JOIN`
**Ejemplo**: Seleccionar todos los empleados y sus departamentos, incluyendo aquellos que no tienen departamento asignado.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
LEFT JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

### 5.3 `RIGHT JOIN`
**Ejemplo**: Seleccionar todos los departamentos y los empleados asignados, incluyendo aquellos departamentos sin empleados.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
RIGHT JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

### 5.4 `FULL OUTER JOIN`
**Ejemplo**: Seleccionar todos los empleados y departamentos, mostrando toda la información disponible aunque no haya coincidencias.
```sql
SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
FULL OUTER JOIN departamentos ON empleados.departamento_id = departamentos.id;
```

## 6. Operaciones sobre Tablas

### 6.1 `CREATE TABLE`
**Ejemplo**: Crear una tabla llamada `empleados` con columnas `id`, `nombre`, `edad`, y `salario`.
```sql
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    salario DECIMAL(10, 2)
);
```

### 6.2 `INSERT INTO`
**Ejemplo**: Insertar un nuevo empleado en la tabla `empleados`.
```sql
INSERT INTO empleados (id, nombre, edad, salario)
VALUES (1, 'Juan', 28, 30000.00);
```

### 6.3 `UPDATE`
**Ejemplo**: Aumentar el salario de los empleados del departamento de 'IT' en un 10%.
```sql
UPDATE empleados
SET salario = salario * 1.1
WHERE departamento = 'IT';
```

### 6.4 `DELETE`
**Ejemplo**: Eliminar a los empleados cuya edad sea menor a 25.
```sql
DELETE FROM empleados
WHERE edad < 25;
```

## 7. Consultas Complejas

### 7.1 Subconsultas
**Ejemplo**: Seleccionar los nombres de los empleados cuyo salario sea mayor que el salario promedio de todos los empleados.
```sql
SELECT nombre
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);
```

### 7.2 Funciones de Ventana
**Ejemplo**: Asignar un ranking a los empleados basado en su salario.
```sql
SELECT nombre, salario, RANK() OVER (ORDER BY salario DESC) AS ranking
FROM empleados;
```

## 8. Operadores de Unión y Set

### 8.1 `UNION` y `UNION ALL`
**Ejemplo**: Seleccionar los empleados del departamento 'IT' y aquellos con salario mayor a 50,000.
```sql
SELECT nombre FROM empleados WHERE departamento = 'IT'
UNION
SELECT nombre FROM empleados WHERE salario > 50000;
```

## 9. Índices

### 9.1 `CREATE INDEX`
**Ejemplo**: Crear un índice sobre la columna `nombre` para mejorar la velocidad de las búsquedas.
```sql
CREATE INDEX idx_nombre ON empleados(nombre);
```

## 10. Cláusula `DISTINCT`
**Ejemplo**: Seleccionar todos los departamentos sin repetirlos.
```sql
SELECT DISTINCT departamento FROM empleados;
```

## 11. Operaciones de Fecha y Hora

### 11.1 Funciones de Fecha
**Ejemplo**: Seleccionar empleados contratados el 1 de enero de 2023.
```sql
SELECT nombre FROM empleados WHERE DATE(contratacion) = '2023-01-01';
```

## 12. Transacciones

### 12.1 `BEGIN`, `COMMIT`, `ROLLBACK`
**Ejemplo**: Agrupar operaciones para aumentar el salario y eliminar empleados según ciertas condiciones.
```sql
BEGIN;
UPDATE empleados SET salario = salario * 1.05 WHERE departamento = 'Ventas';
DELETE FROM empleados WHERE edad < 25;
COMMIT;
```

## 13. Cláusula `CASE`
**Ejemplo**: Categorizar a los empleados según su salario.
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
**Ejemplo**: Concatenar el nombre y apellido de los empleados.
```sql
SELECT CONCAT(nombre, ' ', apellido) AS nombre_completo
FROM empleados;
```

## 15. Conclusión

Estos ejemplos complementarios permiten visualizar la aplicación práctica de los comandos y funciones descritos en la guía principal de SQL. Practicar estos ejemplos ayudará a obtener una mayor comprensión de cada comando y su uso adecuado en diferentes situaciones.
