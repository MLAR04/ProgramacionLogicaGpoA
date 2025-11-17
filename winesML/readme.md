# ML - Gonzalez Navarro

## Instrucciones

Instrucciones paso a paso

Importar librerías necesarias:

```python
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
```

Estas librerías permiten:


* load_wine → cargar la base de datos del vino.
* DecisionTreeClassifier → crear el clasificador basado en reglas.
* export_text → visualizar las reglas aprendidas.
* train_test_split → dividir los datos en entrenamiento y prueba.

Cargar el dataset del vino:

```python
wine = load_wine()
x, y = wine.data, wine.target
```

Donde:
* x contiene las características químicas del vino (ej. alcohol, ácido málico, flavonoides, etc.)
* y contiene la clase del vino (0, 1 o 2, que corresponden a 3 tipos de vino).

Dividir los datos en entrenamiento y prueba:
* 80% de los datos se usan para entrenar.
* 20% se reservan para probar la precisión.

Crear y entrenar el clasificador:

* max_depth=2 limita la profundidad del árbol para que las reglas sean más fáciles de interpretar.

Exportar y visualizar las reglas simbólicas:

```python
rules = export_text(tree, feature_names=wine.feature_names)
print(rules)
```


## **Respuesta a las preguntas de la actividad:**


### ¿Cúales son tus opiniones de los resultados?

Personalmente el ML es un tema que me apasiona, y ver en un dataset como varía la precisión me parece muy curioso dependiendo del objetivo que tengamos. En especial en casos como estos, comparándolo con nuestro sistema experto, ya que si nuestro objetivo es generalizar algo, entonces es mejor limitar la profundidad hasta un nivel donde el clasificador generalice bien. Sin embargo si nuestro objetivo es obtener algo muy específico como lo hace un sistema experto, entonces parece mejor opción no limitar al modelo.

### ¿Si crees qué tu base de conocimiento cumple con los requerimientos para utilizarse en un modelo de árbol de decisiones?

En concreto hablando del sistema experto automotriz, creo que la base de conocimiento en sí misma, hablando en concreto de las reglas, es una representación de un modelo sin limitaciones en la profundidad de aprendizaje, construído manualmente. Con esto dicho considero que como tal, no cumple con las condiciones necesarias para utilizarse en un modelo de árbol de decisiones. 

### Justificación

El motivo principal radica en que los hechos de nuestra base de conocimientos están muy generalizados, ya que nuestro motor de inferencia utiliza encadenamiento hacia adelante, por lo que a partir de los síntomas ingresados por el usuario se generan los hechos y se realiza el encadenamiento. Para que nuestra base de conocimientos cumpliera con los requisitos necesitariamos de entrada generar un dataset con información relevante sobre los tipos de fallas, clasificación por sistemas, datos de algunas fallas de vehículos específicos y algunos otros datos más únicamente para poder entrenar el modelo. 

Además también tendríamos que tener en cuenta que, dicho modelo tendría que entrenarse de forma que no se limite la profundidad del árbol, esto por que buscamos respuestas muy específicas, no generalizaciones. Pero también he de decir que un sistema de clasificación de tipos de fallas es una idea bastante atractiva.

### ¿Árbol de regresión?

Si nuestro objetivo fuese obtener valores numéricos, o realizar el cálculo promedio de algún nivel en específico de algún auto, sería posible. Sin embargo, no es el caso, por lo que no considero posible la implementación de árboles de regresión sin hacer una cantidad de ajustes muy grande.