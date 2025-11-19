# Árbol de Decisión – Wine Dataset
  ## Emely Jimena Martinez Rios-22760567

Este proyecto entrena un modelo de clasificación usando un Árbol de Decisión sobre el dataset Wine de Scikit-learn.
El objetivo es analizar cómo cambia la precisión y la complejidad del modelo al ajustar el parámetro max_depth.

## Instalación

1. pip install scikit-learn
2. pip install numpy
3. pip install scipy

## Los 3 ejemplos que realice fueron:
1. max_depth = 1 
      Precisión: 0.66
Reglas:
  color_intensity <= 3.82 → class 1
  color_intensity > 3.82 → class 0
Análisis:
  •	Árbol demasiado simple.
  •	Solo usa una característica.
  •	Baja capacidad predictiva.

• 2. max_depth = 3
     Precisión: 0.94
Reglas principales:
  •	color_intensity
  •	proline
  •	ash
  •	flavanoids
Análisis:
  •	Excelente equilibrio entre profundidad y precisión.
  •	Reglas claras e interpretables.
  •	El mejor modelo de los tres.

• 3. max_depth = None
     Precisión: 0.94
Reglas: 
     Árbol muy profundo, agrega alcohol y más condiciones.
Análisis:
•	Tiende al sobreajuste.
•	Sin mejora real de precisión.
•	Menos interpretable.

## Opinion de los resultados
• El dataset Wine es muy adecuado para árboles de decisión porque:
    1. Es numérico
    2. Tiene clases claras y balanceadas
    3. No tiene datos faltantes
    4. El árbol produce reglas interpretables
    5. Las características químicas permiten separaciones lógicas
• El modelo con max_depth = 3 es el mejor, ya que logra:
    1. Alta precisión
    2. Reglas comprensibles
    3. No se sobreajusta

## ¿Mi base de conocimiento cumple para un árbol de decisión? y Justificacion 
  • Si, si cumple, ya que tiene 13 caracteristicas para dividir los datos, las clases son claras y se diferencian quimicamente, 
    no contiene valores faltantes ni excesivo. Ademas que el modelo logra precision con la profundidad moderada, el arbol genera       reglas coheremtes y faciles de interpretar. Por ultimo las variables quimicas como: color_intensity, flavanoids y proline          logra la definicion clara para clasificar los vinos. 

## Características:
13 variables químicas, las cuales son: 
  1. alcohol
  2. malic_acid (ácido málico)
  3. ash (cenizas)
  4. alcalinity_of_ash (alcalinidad de las cenizas)
  5. magnesium (magnesio)
  6. total_phenols (fenoles totales)
  7. flavanoids (flavonoides)
  8. nonflavanoid_phenols (fenoles no flavonoides)
  9. proanthocyanins (proantocianinas)
  10. color_intensity (intensidad del color)
  11. hue (matiz del color)
  12. od280/od315_of_diluted_wines (índice OD280/OD315)
  13. proline (aminoácido prolina)
      
 ## Clases:
 0, 1 y 2 (tres tipos de vino) 



