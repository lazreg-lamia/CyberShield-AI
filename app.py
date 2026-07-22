import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from network_analysis import analyze_network
from PIL import Image

logo = Image.open("assets/logo.png")

st.image(logo, width=170)

# ==========================
# Configuration
# ==========================

st.set_page_config(
    page_title="CyberShield-AI",
    page_icon="🛡️",
    layout="wide"
)

# ==========================
# Titre
# ==========================

st.image(logo, width=170)
st.title("CyberShield-AI")

st.subheader(
    "Détection intelligente d'intrusions réseau par Intelligence Artificielle"
)

st.divider()

# ==========================
# Informations principales
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Modèle IA",
        "Random Forest"
    )

with col2:
    st.metric(
        "Version",
        "v1.0"
    )

with col3:
    st.metric(
        "Statut",
        "🟢 Prêt"
    )

st.divider()

# ==========================
# Import du dataset
# ==========================

st.header("📂 Import du dataset")

uploaded_file = st.file_uploader(
    "Sélectionnez un fichier CSV",
    type=["csv"]
)

if uploaded_file is None:

    st.info(
        "Veuillez sélectionner un dataset pour commencer."
    )

    st.stop()

# ==========================
# Aperçu du dataset
# ==========================

df = pd.read_csv(uploaded_file)

st.success("✅ Dataset chargé avec succès")

st.write("### Aperçu")

st.dataframe(df.head())

uploaded_file.seek(0)
# ==========================
# Bouton d'analyse
# ==========================

st.divider()

if st.button(
    "▶️ Lancer l'analyse",
    use_container_width=True
):

    uploaded_file.seek(0)

    with st.spinner(
        "Analyse du réseau en cours..."
    ):

        results = analyze_network(
            uploaded_file
        )

    st.success(
        "Analyse terminée avec succès !"
    )

    # ==========================
    # Résumé
    # ==========================

    st.divider()

    st.header("📊 Résumé de l'analyse")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Connexions analysées",
            len(results["prediction_labels"])
        )

    with col2:

        st.metric(
            "Connexions normales",
            results["benign_count"]
        )

    with col3:

        st.metric(
            "Attaques détectées",
            results["attack_count"]
        )

    with col4:

        st.metric(
            "État du réseau",
            results["network_status"]
        )

    st.metric(
        "Temps d'analyse",
        f"{results['analysis_time']:.3f} s"
    )
    # ==========================
    # Répartition des risques
    # ==========================

    st.divider()

    st.header("⚠️ Répartition des risques")

    risk_df = pd.DataFrame({

        "Niveau de risque":
        list(results["risk_counter"].keys()),

        "Nombre":
        list(results["risk_counter"].values())

    })

    st.bar_chart(

        risk_df.set_index(
            "Niveau de risque"
        )

    )


    pie_df = pd.DataFrame({
        "Catégorie":["Normales","Attaques"],
        "Nombre":[results["benign_count"],results["attack_count"]]
    })
    st.write("### Répartition Normales / Attaques")
    st.pyplot(pie_df.set_index("Catégorie").plot.pie(y="Nombre", autopct="%1.1f%%", legend=False).get_figure())

    # ==========================
    # Détail des attaques
    # ==========================

    st.divider()

    st.header("🚨 Attaques détectées")

    if results["attack_count"] == 0:

        st.success(
            "Aucune attaque détectée."
        )

    else:

        attack_df = pd.DataFrame({

            "Type d'attaque":
            list(results["attack_types"].keys()),

            "Nombre":
            list(results["attack_types"].values())

        })

        st.dataframe(
            attack_df,
            use_container_width=True
        )
     # ==========================
    # Rapport complet
    # ==========================

    st.divider()

    st.header("📋 Rapport complet")

    st.dataframe(
        results["report"],
        use_container_width=True
    )

    # ==========================
    # Informations techniques
    # ==========================

    st.divider()

    st.header("⚙️ Informations techniques")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**ID Analyse :** {results['analysis_id']}"
        )

        st.write(
            f"**Date :** {results['report_date']}"
        )

        st.write(
            f"**Type :** {results['analysis_type']}"
        )

        st.write(
            f"**Version :** {results['software_version']}"
        )

        st.write(
            f"**Modèle :** {results['model_name']}"
        )

        st.write(
            f"**Dataset :** {results['dataset_name']}"
        )

    with col2:

        st.write(
            f"**Caractéristiques utilisées :** {results['features_used']}"
        )

        st.write(
            f"**Connexions du dataset :** {results['total_dataset_connections']}"
        )

        st.write(
            f"**Caractéristiques du dataset :** {results['dataset_features']}"
        )

        st.write(
            f"**Système :** {results['operating_system']}"
        )

        st.write(
            f"**Python :** {results['python_version']}"
        )

        st.write(
            f"**Développeur :** {results['developer']}"
        )
    # ==========================
    # Téléchargement des rapports
    # ==========================

    st.divider()

    st.header("📥 Télécharger les rapports")

    col1, col2, col3 = st.columns(3)

    with col1:

        with open(
            "results/analysis_summary.txt",
            "rb"
        ) as file:

            st.download_button(

                label="📄 Résumé TXT",

                data=file,

                file_name="analysis_summary.txt",

                mime="text/plain",

                use_container_width=True

            )

    with col2:

        csv_report = results["report"].to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(

            label="📊 Rapport CSV",

            data=csv_report,

            file_name="network_analysis_report.csv",

            mime="text/csv",

            use_container_width=True

        )

    with col3:

        csv_statistics = results[
            "statistics"
        ].to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(

            label="📈 Statistiques CSV",

            data=csv_statistics,

            file_name="analysis_statistics.csv",

            mime="text/csv",

            use_container_width=True

        )

    # ==========================
    # Pied de page
    # ==========================

    st.divider()

    st.caption(
        "CyberShield-AI v1.0 • Développé par Lazreg Lamia Chiraz"
    )
# ==========================
# Barre latérale
# ==========================

st.sidebar.title(
    "🛡️ CyberShield-AI"
)

st.sidebar.success(
    "Application opérationnelle"
)

st.sidebar.markdown("---")

st.sidebar.write("### Informations")

st.sidebar.write(
    "🤖 Modèle : Random Forest"
)

st.sidebar.write(
    "📦 Version : v1.0"
)

st.sidebar.write(
    "👩‍💻 Développeur :"
)

st.sidebar.write(
    "Lazreg Lamia Chiraz"
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Licence Informatique"
)

st.sidebar.write(
    "Université Djillali Liabès"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Importez un dataset CSV puis cliquez sur "
    "'Lancer l'analyse' pour détecter les "
    "intrusions réseau."
)                       