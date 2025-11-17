from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

## Por lo que comprendo, aquí se carga el dataset en una variable
wine = load_wine()
x,y = wine.data,wine.target

## Para dividir los datos en entrenamiento y prueba se usa el metodo train_test_split() y el test_size es para asignar un porcentaje de los datos a pruebas
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2,random_state=42)

## Imprimiré los datos de entrenamiento y prueba para verificar que la estructura es correcta
print(f"Datos de entrenamiento: {x_train.shape[0]} muestras")
print(f"Datos de prueba: {x_test.shape[0]} muestras")

## En esta parte se crea y entrena el clasificador y se usa finalmente la clase DecisionTreeClassifier con la profundidad limitada
tree = DecisionTreeClassifier(max_depth=2)

## Dejo comentado el juego con la profundidad
## tree = DecisionTreeClassifier(max_depth=None)
tree.fit(x_train, y_train)

## Finalmente se usa el método export_text() para exportar las reglas aprendidas por el clasificador
rules = export_text(tree, feature_names=wine.feature_names)

## Imprimo las reglas para ver que hay
print("Reglas del árbol")
print(rules)

## Evaluo la precisión
train_accuracy = tree.score(x_train, y_train)
test_accuracy = tree.score(x_test, y_test)

## Imprimo los resultados de la evaluación
print(f"\nPrecisión en entrenamiento: {train_accuracy:.2f}")
print(f"Precisión en prueba: {test_accuracy:.2f}")

