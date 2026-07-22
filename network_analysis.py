import joblib
import pandas as pd
import numpy as np
import time
import platform
import sys

from datetime import datetime
from collections import Counter


def analyze_network(dataset):

# ==========================
# Début de l'analyse
# ==========================

    start_analysis = time.time()

# ==========================
# Chargement du modèle
# ==========================

    model = joblib.load(
        "models/cybershield_ai_model.pkl"
    )

    encoder = joblib.load(
        "models/label_encoder.pkl"
    )

# ==========================
# Chargement du dataset
# Compatible Terminal + Streamlit
# ==========================

    if isinstance(dataset, str):

        df = pd.read_csv(dataset)

        dataset_name = dataset.split("/")[-1]

    else:

        df = pd.read_csv(dataset)

        dataset_name = dataset.name

# ==========================
# Nettoyage
# ==========================

    df.columns = df.columns.str.strip()

    df.dropna(inplace=True)

    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    df.dropna(inplace=True)

# ==========================
# Préparation des données
# ==========================

    X = df.drop(
        "Label",
        axis=1
    )

# ==========================
# Analyse
# ==========================

    predictions = model.predict(
        X
    )

    probabilities = model.predict_proba(
        X
    )

    prediction_labels = encoder.inverse_transform(
        predictions
    )

    confidence_scores = (
        probabilities.max(axis=1) * 100
    )

# ==========================
# Niveaux de risque
# ==========================

    risk_levels = []

    risk_counter = Counter()

    for label in prediction_labels:

        if label == "BENIGN":

            risk = "Faible"

        else:

            risk = "Élevé"

        risk_levels.append(risk)

        risk_counter[risk] += 1

# ==========================
# Comptage des attaques
# ==========================

    attack_types = Counter()

    benign_count = 0

    attack_count = 0

    for label in prediction_labels:

        if label == "BENIGN":

            benign_count += 1

        else:

            attack_count += 1

            attack_types[label] += 1

    attack_percentage = (
        attack_count /
        len(prediction_labels)
    ) * 100

# ==========================
# État du réseau
# ==========================

    if attack_percentage == 0:

        network_status = "Sain"

    elif attack_percentage < 10:

        network_status = "Sous surveillance"

    else:

        network_status = "Compromis"

# ==========================
# Informations générales
# ==========================

    report_date = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    analysis_id = datetime.now().strftime(
        "ANALYSIS-%Y%m%d-%H%M%S"
    )

    analysis_type = (
        "Analyse complète du dataset"
    )

    software_version = (
        "CyberShield-AI v1.0"
    )

    model_name = "Random Forest"

    features_used = X.shape[1]

    available_models = 2

    total_dataset_connections = len(df)

    dataset_features = len(df.columns) - 1

    developer = (
        "Lazreg Lamia Chiraz"
    )

    operating_system = platform.system()

    python_version = sys.version.split()[0]

    model_file = (
        "cybershield_ai_model.pkl"
    )

# ==========================
# Création du rapport
# ==========================

    report = pd.DataFrame({

        "ID Analyse":
        [analysis_id] * len(prediction_labels),

        "Date du rapport":
        [report_date] * len(prediction_labels),

        "Type d'analyse":
        [analysis_type] * len(prediction_labels),

        "Version":
        [software_version] * len(prediction_labels),

        "Modèle IA":
        [model_name] * len(prediction_labels),

        "Caractéristiques utilisées":
        [features_used] * len(prediction_labels),

        "Modèles disponibles":
        [available_models] * len(prediction_labels),

        "Dataset":
        [dataset_name] * len(prediction_labels),

        "Connexions du dataset":
        [total_dataset_connections] * len(prediction_labels),

        "Caractéristiques du dataset":
        [dataset_features] * len(prediction_labels),

        "Développeur":
        [developer] * len(prediction_labels),

        "Système d'exploitation":
        [operating_system] * len(prediction_labels),

        "Version Python":
        [python_version] * len(prediction_labels),

        "Version du logiciel":
        [software_version] * len(prediction_labels),

        "Fichier du modèle":
        [model_file] * len(prediction_labels),

        "Connexion":
        range(
            1,
            len(prediction_labels) + 1
        ),

        "Résultat":
        prediction_labels,

        "Niveau de risque":
        risk_levels,

        "Confiance (%)":
        confidence_scores.round(2),

        "État du réseau":
        [network_status] * len(prediction_labels)

    })

# ==========================
# Sauvegarde du rapport complet
# ==========================

    filename = datetime.now().strftime(
        "results/network_analysis_report_%Y%m%d_%H%M%S.csv"
    )

    report.to_csv(
        filename,
        index=False
    )

# ==========================
# Rapport des attaques
# ==========================

    attack_report = report[
        report["Résultat"] != "BENIGN"
    ]

    attack_report.to_csv(
        "results/attacks_only_report.csv",
        index=False
    )

# ==========================
# Temps d'analyse
# ==========================

    analysis_time = (
        time.time() - start_analysis
    )

# ==========================
# Création du résumé TXT
# ==========================

    summary = f"""
========== CyberShield-AI ==========
ID Analyse : {analysis_id}
Date : {report_date}

Type d'analyse : {analysis_type}

Version : {software_version}

Modèle IA : {model_name}

Caractéristiques utilisées : {features_used}

Modèles disponibles : {available_models}

Dataset : {dataset_name}

Connexions du dataset : {total_dataset_connections}

Caractéristiques du dataset : {dataset_features}

Développeur : {developer}

Système d'exploitation : {operating_system}

Version Python : {python_version}

Fichier du modèle : {model_file}

Connexions analysées : {len(prediction_labels)}

Connexions normales : {benign_count}

Attaques détectées : {attack_count}

Pourcentage d'attaques : {round(attack_percentage, 2)} %

État du réseau : {network_status}

Répartition des risques :

- Faible : {risk_counter.get("Faible", 0)}

- Élevé : {risk_counter.get("Élevé", 0)}

Temps total d'analyse : {round(analysis_time, 3)} s
"""

    with open(
        "results/analysis_summary.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(summary)

# ==========================
# Création des statistiques
# ==========================

    statistics = pd.DataFrame({

        "ID Analyse":
        [analysis_id],

        "Date":
        [report_date],

        "Connexions analysées":
        [len(prediction_labels)],

        "Connexions normales":
        [benign_count],

        "Attaques détectées":
        [attack_count],

        "Pourcentage d'attaques":
        [round(attack_percentage, 2)],

        "État du réseau":
        [network_status],

        "Temps d'analyse (s)":
        [round(analysis_time, 3)]

    })

    statistics.to_csv(

        "results/analysis_statistics.csv",

        index=False

    )

# ==========================
# Retour des résultats
# ==========================

    return {

        "analysis_id":
        analysis_id,

        "report_date":
        report_date,

        "analysis_type":
        analysis_type,

        "software_version":
        software_version,

        "model_name":
        model_name,

        "dataset_name":
        dataset_name,

        "prediction_labels":
        prediction_labels,

        "confidence_scores":
        confidence_scores,

        "risk_levels":
        risk_levels,

        "risk_counter":
        risk_counter,

        "attack_types":
        attack_types,

        "benign_count":
        benign_count,

        "attack_count":
        attack_count,

        "attack_percentage":
        attack_percentage,

        "network_status":
        network_status,

        "analysis_time":
        analysis_time,

        "report":
        report,

        "statistics":
        statistics,

        "features_used":
        features_used,

        "available_models":
        available_models,

        "total_dataset_connections":
        total_dataset_connections,

        "dataset_features":
        dataset_features,

        "developer":
        developer,

        "operating_system":
        operating_system,

        "python_version":
        python_version,

        "model_file":
        model_file

    }

# ==========================
# Exécution directe
# ==========================

if __name__ == "__main__":

    sample_dataset = (
        "data/network/MachineLearningCVE/"
        "Tuesday-WorkingHours.pcap_ISCX.csv"
    )

    results = analyze_network(
        sample_dataset
    )

    print("\n==============================")
    print("CyberShield-AI")
    print("==============================")

    print(
        f"Analyse : {results['analysis_id']}"
    )

    print(
        f"État du réseau : {results['network_status']}"
    )

    print(
        f"Attaques détectées : {results['attack_count']}"
    )

    print(
        f"Connexions normales : {results['benign_count']}"
    )

    print(
        f"Temps d'analyse : "
        f"{results['analysis_time']:.3f} s"
    )

    print("\nRapports générés dans le dossier results/")               