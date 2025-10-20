# 🍽️ Práctica de Resolución SLD: El Plato del Buen Comer

Este proyecto es una implementación de un motor de **Resolución SLD (Selective Linear Definite clause)** simple, escrito en Python.

El objetivo del script `sld_practica.py` es evaluar, basándose en un conjunto de reglas y hechos lógicos, si una comida se considera "saludable" según una versión simplificada del **Plato del Buen Comer**. El script recibe una consulta (query) y, si tiene éxito, devuelve las sustituciones de variables y la ruta de derivación paso a paso que utilizó para encontrar la solución.



## 🧑‍💻 Información del Alumno

* **Nombre:** Jesús Martínez
* **Número de Control:** 22760568

## 📚 Base de Conocimiento

La base de conocimiento define los hechos (lo que sabemos que es verdad) y las reglas (cómo inferir nueva información) sobre los alimentos y las comidas.

### Hechos

Los hechos definen los grupos de alimentos, las comidas existentes y qué grupos contiene cada comida.

```python
# 1. Grupos de alimentos
(["grupo", "frutas"], [])
(["grupo", "verduras"], [])
(["grupo", "cereales"], [])
(["grupo", "leguminosas"], [])
(["grupo", "origen_animal"], [])

# 2. Comidas y su contenido
(["comida", "comida1"], [])
(["contiene", "comida1", "frutas"], [])
(["contiene", "comida1", "verduras"], [])
(["contiene", "comida1", "cereales"], [])

(["comida", "comida2"], [])
(["contiene", "comida2", "origen_animal"], [])
(["contiene", "comida2", "cereales"], [])

# (También se definen alimentos específicos como 'manzana' o 'pollo',
# aunque la regla principal opera a nivel de 'grupos')