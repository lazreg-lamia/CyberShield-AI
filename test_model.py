import joblib
import pandas as pd

# Charger le modèle entraîné
model = joblib.load("models/cybershield_ai_model.pkl")

# Charger le LabelEncoder
encoder = joblib.load("models/label_encoder.pkl")

# Charger le dataset
df = pd.read_csv(
    "data/network/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv"
)

# Supprimer les espaces dans les noms de colonnes
df.columns = df.columns.str.strip()

# Séparer les caractéristiques (X)
X = df.drop("Label", axis=1)

# Remplacer les valeurs infinies
X = X.replace([float("inf"), float("-inf")], 0)

# Remplacer les valeurs manquantes
X = X.fillna(0)

# Faire les prédictions sur tout le dataset
predictions = model.predict(X)

# Convertir les numéros en noms de classes
prediction_labels = encoder.inverse_transform(predictions)

# Afficher les 10 premières prédictions
print("Les 10 premières prédictions :")
print(prediction_labels[:10])

# Ajouter les prédictions au DataFrame
df["Prediction"] = prediction_labels

# Afficher les 10 premières lignes
print(df[["Label", "Prediction"]].head(10))

# Sauvegarder le résultat
df.to_csv("results/predictions.csv", index=False)

print("Les prédictions ont été enregistrées dans predictions.csv")

# Trouver les erreurs du modèle
errors = df[df["Label"] != df["Prediction"]]

print("Nombre d'erreurs :", len(errors))

print(errors[["Label", "Prediction"]].head(10))

error_rate = (len(errors) / len(df)) * 100

print(f"Taux d'erreur : {error_rate:.4f}%")

# Sauvegarder uniquement les erreurs
errors.to_csv("results/prediction_errors.csv", index=False)

print("Les erreurs ont été enregistrées dans prediction_errors.csv")