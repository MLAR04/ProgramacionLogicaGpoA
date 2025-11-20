# Clasificación con Árbol de Decisión - Wine Dataset

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# 1. Cargar el dataset
wine = load_wine()
X, y = wine.data, wine.target

# 2. Dividir en entrenamiento y prueba (80% - 20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Crear el clasificador con profundidad limitada
tree = DecisionTreeClassifier(max_depth=2, random_state=42)

# 4. Entrenar el modelo
tree.fit(X_train, y_train)

# 5. Mostrar reglas aprendidas
rules = export_text(tree, feature_names=wine.feature_names)
print("Reglas del árbol con max_depth=2:\n")
print(rules)

# 6. Evaluar precisión
accuracy = tree.score(X_test, y_test)
print("Precisión en datos de prueba:", accuracy)


# ===============================
# EXTRA: probar diferentes profundidades
# ===============================

print("\n\n=======================")
print(" PRUEBAS CON max_depth")
print("=======================\n")

for depth in [1, 2, 3, None]:
    print("\n==============================")
    print(f" Árbol con max_depth={depth}")
    print("==============================")

    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)

    print(export_text(tree, feature_names=wine.feature_names))
    print("Precisión:", tree.score(X_test, y_test))
