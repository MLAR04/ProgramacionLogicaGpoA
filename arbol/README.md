# Clasificación con Árbol de Decisión – Wine Dataset


Opinión sobre los resultados

El modelo logra una **buena precisión** cuando se usa una profundidad moderada (por ejemplo max_depth=2 o 3), ya que el árbol mantiene reglas claras y generales.  
Cuando el árbol se entrena sin límite (max_depth=None), se vuelve demasiado complejo y existe riesgo de overfitting, lo que significa que aprende reglas demasiado específicas.

 Pruebas realizadas
- `max_depth = 1
- `max_depth = 2
- `max_depth = 3
- `max_depth = 4
- `max_depth = None (sin límite)

 ¿El dataset cumple los requisitos para un árbol de decisión?

-Sí cumple.

Justificación
- Contiene características numéricas claramente definidas.
- Las clases son categorías discretas (0, 1, 2).
- No tiene valores faltantes.
- Es un dataset bien estructurado y clásico para clasificación.

¿Se podría usar regresión?

No.  
La regresión predice valores numéricos continuos, pero este dataset tiene clases.  
Por lo tanto, la regresión no es adecuada para este problema.

RESULTADO
Reglas del árbol con max_depth=2:

|--- color_intensity <= 3.82
|   |--- proline <= 1002.50
|   |   |--- class: 1
|   |--- proline >  1002.50
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.40
|   |   |--- class: 2
|   |--- flavanoids >  1.40
|   |   |--- class: 0

Precisión en datos de prueba: 0.8611111111111112


=======================
 PRUEBAS CON max_depth
=======================


==============================
 Árbol con max_depth=1
==============================
|--- color_intensity <= 3.82
|   |--- class: 1
|--- color_intensity >  3.82
|   |--- class: 0

Precisión: 0.6666666666666666

==============================
 Árbol con max_depth=2
==============================
|--- color_intensity <= 3.82
|   |--- proline <= 1002.50
|   |   |--- class: 1
|   |--- proline >  1002.50
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.40
|   |   |--- class: 2
|   |--- flavanoids >  1.40
|   |   |--- class: 0

Precisión: 0.8611111111111112

==============================
 Árbol con max_depth=3
==============================
|--- color_intensity <= 3.82
|   |--- proline <= 1002.50
|   |   |--- ash <= 3.07
|   |   |   |--- class: 1
|   |   |--- ash >  3.07
|   |   |   |--- class: 0
|   |--- proline >  1002.50
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.40
|   |   |--- class: 2
|   |--- flavanoids >  1.40
|   |   |--- proline <= 724.50
|   |   |   |--- class: 1
|   |   |--- proline >  724.50
|   |   |   |--- class: 0

Precisión: 0.9444444444444444

==============================
 Árbol con max_depth=None
==============================
|--- color_intensity <= 3.82
|   |--- proline <= 1002.50
|   |   |--- ash <= 3.07
|   |   |   |--- class: 1
|   |   |--- ash >  3.07
|   |   |   |--- class: 0
|   |--- proline >  1002.50
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.40
|   |   |--- class: 2
|   |--- flavanoids >  1.40
|   |   |--- proline <= 724.50
|   |   |   |--- alcohol <= 13.14
|   |   |   |   |--- class: 1
|   |   |   |--- alcohol >  13.14
|   |   |   |   |--- class: 0
|   |   |--- proline >  724.50
|   |   |   |--- class: 0

Precisión: 0.9444444444444444

Process finished with exit code 0
