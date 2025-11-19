from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

wine = load_wine()
X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

tree = DecisionTreeClassifier(max_depth=None, random_state=42)

tree.fit(X_train, y_train)

accuracy = tree.score(X_test, y_test)
print("Precisión en datos de prueba:", accuracy)

rules = export_text(tree, feature_names=wine.feature_names)
print("\n--- Reglas del Árbol ---")
print(rules)
