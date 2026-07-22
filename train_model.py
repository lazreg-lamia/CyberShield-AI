import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
import time
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# ==========================
# Chargement du dataset
# ==========================

df = pd.read_csv(
    "data/network/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv"
)

# ==========================
# Nettoyage
# ==========================

df.columns = df.columns.str.strip()
df = df.dropna()

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# ==========================
# Séparation des données
# ==========================

X = df.drop("Label", axis=1)
y = df["Label"]

# ==========================
# Encodage
# ==========================

encoder = LabelEncoder()
y = encoder.fit_transform(y)

print("Classes apprises :")
print(encoder.classes_)

print("\nNombre d'exemples par classe :")
print(df["Label"].value_counts())

# ==========================
# Train / Test
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Decision Tree
# ==========================

model = DecisionTreeClassifier(random_state=42)

start = time.time()

model.fit(X_train, y_train)

decision_tree_time = time.time() - start

print(
    "Temps d'entraînement Decision Tree :",
    round(decision_tree_time, 3),
    "secondes"
)
print("\nLe modèle est entraîné !")

y_pred = model.predict(X_test)

print(y_pred[:10])
print(y_test[:10])

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", accuracy)

cm = confusion_matrix(y_test, y_pred)

print("\nMatrice de confusion :")
print(cm)

print("\nClassification Report :")
print(classification_report(
    y_test,
    y_pred,
    target_names=encoder.classes_
))

# ==========================
# Random Forest
# ==========================

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Temps d'entraînement
start = time.time()

rf_model.fit(X_train, y_train)

random_forest_time = time.time() - start

print(
    "Temps d'entraînement Random Forest :",
    round(random_forest_time, 3),
    "secondes"
)

# Temps de prédiction
start = time.time()

rf_pred = rf_model.predict(X_test)

prediction_time = time.time() - start

print(
    "Temps de prédiction :",
    round(prediction_time, 4),
    "secondes"
)

rf_accuracy = accuracy_score(y_test, rf_pred)

print(
    "\nRandom Forest Accuracy :",
    rf_accuracy
)

# ==========================
# Sauvegarde
# ==========================

joblib.dump(
    rf_model,
    "models/cybershield_ai_model.pkl"
)

print("\nModèle sauvegardé avec succès !")

joblib.dump(
    encoder,
    "models/label_encoder.pkl"
)

print("LabelEncoder sauvegardé avec succès !")

# Taille du modèle
model_size = os.path.getsize(
    "models/cybershield_ai_model.pkl"
) / (1024 * 1024)

print(
    "Taille du modèle :",
    round(model_size, 2),
    "Mo"
)

# Temps de chargement
start = time.time()

loaded_model = joblib.load("models/cybershield_ai_model.pkl")

loading_time = time.time() - start

print(
    "Temps de chargement du modèle :",
    round(loading_time, 4),
    "secondes"
)

# ==========================
# Comparaison des modèles
# ==========================

comparison = pd.DataFrame({
    "Modèle": [
        "Decision Tree",
        "Random Forest"
    ],
    "Accuracy": [
        accuracy,
        rf_accuracy
    ],
    "Temps entraînement (s)": [
        round(decision_tree_time, 3),
        round(random_forest_time, 3)
    ],
    "Temps prédiction (s)": [
        "-",
        round(prediction_time, 4)
    ],
    "Temps chargement (s)": [
        "-",
        round(loading_time, 4)
    ],
    "Taille (Mo)": [
        "-",
        round(model_size, 2)
    ]
})

print("\nComparaison des modèles :")
print(comparison)

comparison.to_csv(
    "results/model_comparison.csv",
    index=False
)

plt.figure(figsize=(6, 5))

plt.bar(
    comparison["Modèle"],
    comparison["Accuracy"]
)

plt.title("Comparaison des modèles")
plt.xlabel("Modèle")
plt.ylabel("Accuracy")

plt.ylim(0.99, 1.00)

plt.tight_layout()

plt.savefig("results/model_comparison.png")

plt.show()

# ==========================
# Importance des variables
# ==========================

importance = pd.Series(
    rf_model.feature_importances_,
    index=X.columns
)

print("\nTop 10 des caractéristiques les plus importantes :")
print(
    importance
    .sort_values(ascending=False)
    .head(10)
)

top10 = importance.sort_values(ascending=False).head(10)

top10.to_csv(
    "results/top10_features.csv",
    header=["Importance"]
)

plt.figure(figsize=(10, 6))

top10.plot(kind="bar")

plt.title("Top 10 des caractéristiques les plus importantes")
plt.xlabel("Caractéristiques")
plt.ylabel("Importance")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("results/top10_features.png")

plt.show()

# ==========================
# Graphique de répartition
# ==========================

plt.figure(figsize=(8, 5))

df["Label"].value_counts().plot(kind="bar")

plt.title("Répartition des classes")
plt.xlabel("Type de connexion")
plt.ylabel("Nombre d'exemples")

plt.tight_layout()

plt.savefig("results/class_distribution.png")

plt.show()