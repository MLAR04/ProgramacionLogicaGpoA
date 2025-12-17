from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
import pandas as pd

# ===============================
# 1. Cargar el dataset Wine
# ===============================
wine = load_wine()

# ===============================
# 2. Ver información del dataset
# ===============================
print("=== DESCRIPCIÓN DEL DATASET ===")
print(wine.DESCR)

print("\n=== NOMBRES DE LAS CARACTERÍSTICAS ===")
print(wine.feature_names)

print("\n=== CLASES DEL DATASET ===")
print(wine.target_names)

print("\n=== TAMAÑO DEL DATASET ===")
print("Número de muestras:", wine.data.shape[0])
print("Número de características:", wine.data.shape[1])

# ===============================
# 3. Convertir a DataFrame (tabla)
# ===============================
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["clase"] = wine.target

print("\n=== PRIMERAS 5 FILAS DEL DATASET ===")
print(df.head())

# ===============================
# 4. Preparar datos
# ===============================
X = wine.data
y = wine.target

# División 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# 5. Crear y entrenar el Árbol de Decisión
# ===============================
tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train, y_train)

# ===============================
# 6. Evaluar precisión
# ===============================
print("\n=== PRECISIÓN DEL MODELO ===")
print("Precisión en datos de prueba:", tree.score(X_test, y_test))

# ===============================
# 7. Mostrar reglas del árbol
# ===============================
rules = export_text(tree, feature_names=wine.feature_names)
print("\n=== REGLAS DEL ÁRBOL DE DECISIÓN ===")
print(rules)
