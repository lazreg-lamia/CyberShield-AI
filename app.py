import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image

from network_analysis import analyze_network


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="CyberShield-AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

logo = Image.open("assets/logo.png")

left, center, right = st.columns([1,2,1])

with center:

    st.markdown("<br>", unsafe_allow_html=True)

    st.image(
        logo,
        width=220
    )

    st.markdown(
        """
        <h1 style="
        text-align:center;
        font-size:64px;
        font-weight:800;
        color:white;
        margin-top:-10px;
        margin-bottom:0px;
        ">
        Cyber<span style="color:#2B8FFF;">Shield</span>-AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="
        text-align:center;
        color:#D8E8FF;
        font-size:24px;
        margin-top:5px;
        margin-bottom:45px;
        ">
        AI-Powered Network Intrusion Detection System
        </p>
        """,
        unsafe_allow_html=True
    )

# ==========================================================
# GLOBAL STYLE
# ==========================================================

st.markdown("""
<style>

/* ---------- Fond général ---------- */

.stApp{
background:linear-gradient(135deg,#07162D,#0A2F73,#0E4DAA);
background-attachment:fixed;
}

/* Cache le header Streamlit */

header{
visibility:hidden;
}

/* Cache le menu */

#MainMenu{
visibility:hidden;
}

/* Footer Streamlit */

footer{
visibility:hidden;
}

/* Marge */

.block-container{
padding-top:30px;
padding-left:50px;
padding-right:50px;
}

/* Sidebar */

[data-testid="stSidebar"]{
background:#07162D;
border-right:1px solid rgba(255,255,255,.08);
}

/* Titres */

h1,h2,h3{
color:white;
}

p{
color:#D7E6FF;
}

label{
color:white!important;
}

/* Cartes */

[data-testid="stMetric"]{
background:rgba(18,58,122,.55);
border:1px solid rgba(79,162,255,.35);
border-radius:18px;
padding:20px;
box-shadow:0 0 25px rgba(0,0,0,.20);
}

[data-testid="stMetricValue"]{
color:white;
font-size:38px;
font-weight:700;
}

[data-testid="stMetricLabel"]{
color:#9FD1FF;
}

/* Uploader */

div[data-testid="stFileUploader"]{
background:rgba(12,41,90,.60);
border:1px dashed #2D8DFF;
border-radius:18px;
padding:25px;
}

/* Dataframe */

div[data-testid="stDataFrame"]{
border-radius:18px;
overflow:hidden;
}

/* Boutons */

.stButton>button{
background:linear-gradient(90deg,#0F6CFF,#3399FF);
color:white;
border:none;
border-radius:12px;
height:55px;
font-size:18px;
font-weight:600;
width:100%;
}

.stDownloadButton>button{
border-radius:12px;
}

/* Divider */

hr{
border:0;
height:1px;
background:rgba(255,255,255,.08);
}

/* Upload Card */

.upload-card{

background:rgba(14,44,92,.60);

border:1px solid rgba(73,148,255,.35);

border-radius:22px;

padding:35px;

box-shadow:0 0 35px rgba(0,0,0,.25);

margin-bottom:25px;

}

.metric-card{

background:rgba(13,43,92,.55);

border:1px solid rgba(82,160,255,.25);

border-radius:22px;

padding:25px;

text-align:center;

box-shadow:0 8px 25px rgba(0,0,0,.25);

transition:.25s;

}

.metric-card:hover{

transform:translateY(-4px);

border:1px solid #3C9CFF;

box-shadow:0 12px 35px rgba(60,156,255,.25);

}

.metric-title{

color:#A9D3FF;

font-size:16px;

margin-bottom:8px;

}

.metric-value{

color:white;

font-size:42px;

font-weight:700;

}

.section-title{

font-size:32px;

font-weight:700;

color:white;

margin-top:40px;

margin-bottom:20px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.sidebar.image(
    logo,
    width=170
)

st.sidebar.markdown(
"""
<h2 style="
text-align:center;
color:white;
margin-bottom:5px;
">
Cyber<span style="color:#2B8FFF;">Shield</span>-AI
</h2>

<p style="
text-align:center;
color:#BFD8FF;
font-size:13px;
margin-top:-8px;
">
AI-Powered Intrusion Detection
</p>
""",
unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

st.sidebar.success("🟢 System Operational")

st.sidebar.markdown("---")

st.sidebar.markdown("### INFORMATION")

st.sidebar.write("🧠 **AI Model**")
st.sidebar.write("Random Forest")

st.sidebar.write("")

st.sidebar.write("📦 **Version**")
st.sidebar.write("v1.0")

st.sidebar.write("")

st.sidebar.write("👩🏻‍💻 **Developer**")
st.sidebar.write("Lazreg Lamia Chiraz")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Upload a CSV dataset

↓

Run the AI analysis

↓

View the results

↓

Download the reports
"""
)

# ==========================================================
# DASHBOARD CARDS
# ==========================================================

col1, col2, col3 = st.columns(
    3,
    gap="large"
)
with col1:
    st.metric("🤖 AI Model", "Random Forest")

with col2:
    st.metric("📦 Version", "v1.0")

with col3:
    st.metric("🟢 Status", "Ready")

st.divider()

# ==========================================================
# DATASET IMPORT
# ==========================================================

st.markdown("""
<div class="upload-card">

<h2 style="color:white;margin-bottom:5px;">
📂 New Analysis
</h2>

<p style="color:#D8E8FF;font-size:17px;">
Upload a network traffic dataset in CSV format to let
<b>CyberShield-AI</b> automatically detect malicious
activities using Artificial Intelligence.
</p>

</div>
""", unsafe_allow_html=True)

st.write(
    "Upload a network traffic dataset in CSV format to let "
    "CyberShield-AI detect malicious activities using the trained "
    "Artificial Intelligence model."
)

uploaded_file = st.file_uploader(
    "📁 Drag & Drop your CSV file here or click to browse",
    type=["csv"]
)

if uploaded_file is None:

    st.info(
        "👆 Please upload a CSV dataset to begin the analysis."
    )

    st.stop()

# ==========================================================
# DATASET PREVIEW
# ==========================================================

df = pd.read_csv(uploaded_file)

st.success("✅ Dataset loaded successfully.")

st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

uploaded_file.seek(0)

st.divider()

if st.button(
    "🚀 START AI ANALYSIS",
    use_container_width=True
):

    uploaded_file.seek(0)

    with st.spinner(
        "Analyzing network traffic..."
    ):

        results = analyze_network(uploaded_file)

    st.success("✅ Analysis completed successfully.")

    st.divider()

    # ==========================================================
    # ANALYSIS SUMMARY
    # ==========================================================

    st.header("📊 Analysis Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Analyzed Connections",
            len(results["prediction_labels"])
        )

    with c2:
        st.metric(
            "Normal Traffic",
            results["benign_count"]
        )

    with c3:
        st.metric(
            "Detected Attacks",
            results["attack_count"]
        )

    with c4:
        st.metric(
            "Network Status",
            results["network_status"]
        )

    st.metric(
        "Analysis Time",
        f"{results['analysis_time']:.3f} s"
    )

    st.divider()

    # ==========================================================
    # RISK DISTRIBUTION
    # ==========================================================

    st.header("⚠️ Risk Distribution")

    risk_df = pd.DataFrame({
        "Risk Level": list(results["risk_counter"].keys()),
        "Count": list(results["risk_counter"].values())
    })

    st.bar_chart(
        risk_df.set_index("Risk Level")
    )

    # ==========================================================
    # NORMAL VS ATTACKS
    # ==========================================================

    st.subheader("📈 Normal vs Attacks")

    pie_df = pd.DataFrame({
        "Category": ["Normal", "Attacks"],
        "Count": [
            results["benign_count"],
            results["attack_count"]
        ]
    })

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        pie_df["Count"],
        labels=pie_df["Category"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["#2ECC71", "#E74C3C"]
    )

    ax.axis("equal")

    st.pyplot(fig)

    st.divider()

    # ==========================================================
    # DETECTED ATTACKS
    # ==========================================================

    st.header("🚨 Detected Attacks")

    if results["attack_count"] == 0:

        st.success(
            "No malicious activity was detected."
        )

    else:

        attack_df = pd.DataFrame({
            "Attack Type": list(results["attack_types"].keys()),
            "Occurrences": list(results["attack_types"].values())
        })

        st.dataframe(
            attack_df,
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # COMPLETE REPORT
    # ==========================================================

    st.header("📋 Complete Analysis Report")

    st.dataframe(
        results["report"],
        use_container_width=True
    )

    st.divider()

    # ==========================================================
    # TECHNICAL INFORMATION
    # ==========================================================

    st.header("⚙️ Technical Information")

    left, right = st.columns(2)

    with left:

        st.write(f"**Analysis ID:** {results['analysis_id']}")
        st.write(f"**Analysis Date:** {results['report_date']}")
        st.write(f"**Analysis Type:** {results['analysis_type']}")
        st.write(f"**Software Version:** {results['software_version']}")
        st.write(f"**AI Model:** {results['model_name']}")
        st.write(f"**Dataset:** {results['dataset_name']}")

    with right:

        st.write(f"**Features Used:** {results['features_used']}")
        st.write(f"**Connections:** {results['total_dataset_connections']}")
        st.write(f"**Dataset Features:** {results['dataset_features']}")
        st.write(f"**Operating System:** {results['operating_system']}")
        st.write(f"**Python Version:** {results['python_version']}")
        st.write(f"**Developer:** {results['developer']}")

    st.divider()

    # ==========================================================
    # DOWNLOAD REPORTS
    # ==========================================================

    st.header("📥 Download Reports")

    col1, col2, col3 = st.columns(3)

    with col1:

        with open(
            "results/analysis_summary.txt",
            "rb"
        ) as file:

            st.download_button(
                label="📄 Summary (.txt)",
                data=file,
                file_name="analysis_summary.txt",
                mime="text/plain",
                use_container_width=True
            )

    with col2:

        report_csv = results["report"].to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📊 Analysis Report (.csv)",
            data=report_csv,
            file_name="network_analysis_report.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col3:

        statistics_csv = results["statistics"].to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📈 Statistics (.csv)",
            data=statistics_csv,
            file_name="analysis_statistics.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # SECURITY INSIGHTS
    # ==========================================================

    st.header("🛡️ Security Insights")

    if results["attack_count"] == 0:

        st.success(
            "No malicious activity has been detected. "
            "Your network traffic appears to be secure."
        )

    else:

        st.warning(
            f"{results['attack_count']} suspicious connection(s) "
            "were detected by the AI model."
        )

        st.info(
            "It is recommended to review the detected attacks, "
            "identify compromised hosts and investigate abnormal "
            "network behavior."
        )

    st.divider()

    # ==========================================================
    # ANALYSIS DETAILS
    # ==========================================================

    with st.expander("📄 Analysis Details"):

        st.write(
            "CyberShield-AI analyzes network traffic using a trained "
            "Random Forest model. The uploaded dataset is processed, "
            "classified and summarized before generating downloadable "
            "reports and statistics."
        )

        st.write("**Detection model:** Random Forest")

        st.write(
            f"**Processed connections:** "
            f"{len(results['prediction_labels'])}"
        )

        st.write(
            f"**Execution time:** "
            f"{results['analysis_time']:.3f} seconds"
        )

    st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#C8D8F0;
        padding:20px;
        font-size:15px;
    ">

    <b>CyberShield-AI v1.0</b><br><br>

    AI-Powered Network Intrusion Detection Platform<br><br>

    Developed by <b>Lazreg Lamia Chiraz</b><br>

    Djillali Liabes University • Computer Science

    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# END
# ==========================================================                    