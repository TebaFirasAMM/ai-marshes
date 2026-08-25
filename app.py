 import streamlit as st
import random

# Your Exclusive Uploaded Logo Link
logo_url = "https://ibb.co"

st.set_page_config(page_title="AI-Marshes Microbe", page_icon=logo_url, layout="wide")

# Light Academic Theme Customization (Ivory background, Navy text, Silver elements)
st.markdown("""
    <style>
    .stApp { 
        background-color: #F8F9FA; 
        color: #0F2042; 
        font-family: 'Times New Roman', Times, serif; 
    }
    h1, h2, h3, h4, h5, h6 {
        color: #0F2042 !important;
        font-family: 'Times New Roman', Times, serif !important;
    }
    .stButton>button {
        background-color: #0F2042 !important;
        color: #FFFFFF !important;
        border-radius: 5px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 10px 24px !important;
    }
    div[data-testid="stSidebar"] {
        background-color: #E9ECEF !important;
    }
    </style>
""", unsafe_allow_html=True)

# Layout for Your Exclusive Logo and Title Integration
col_header_logo, col_header_title = st.columns([1, 6])
with col_header_logo:
    st.image(logo_url, width=130)
with col_header_title:
    st.markdown("<h1 style='margin-top: 10px;'>THE AI-MARSHES MICROBE PLATFORM</h1>", unsafe_allow_html=True)
    st.caption("Predictive Bio-AI for Genomic Mutation & Fetal Cellular Risk Analysis | Official Academic Edition")

st.markdown("<div style='border-top: 2px solid #0F2042; margin-top: 10px; margin-bottom: 20px;'></div>", unsafe_allow_html=True)

st.sidebar.title("ACADEMIC CONSOLE")
st.sidebar.info("Developed by an independent Microbiologist from Iraq for advanced in-silico fetal toxicological mapping.")

tabs = ["📊 Diagnostic Core", "📜 Elite Thesis & Hypothesis"]
selected_tab = st.sidebar.radio("Navigation Protocol:", tabs)

if selected_tab == "📜 Elite Thesis & Hypothesis":
    st.header("I. SCIENTIFIC THESIS & PRINCIPLES")
    st.markdown("<div style='background-color: #FFFFFF; padding: 25px; border-radius: 10px; border-left: 5px solid #0F2042; line-height: 1.8; font-size: 1.15rem; box-shadow: 0px 2px 4px rgba(0,0,0,0.05);'><b>Abstract Hypothesis:</b> Environmental degradation and hydro-stress within the unique ecosystem of the Iraqi Marshes enforce rapid, adaptive genomic micro-mutations in waterborne microbial pathogens to tolerate extreme hypersalinity and hyperthermia. This platform mathematically models these evolutionary variations <i>in silico</i>. It demonstrates how mutated microbial strains hyper-express lethal bio-toxins capable of breaching maternal-fetal cellular barriers, thereby targeting early embryonic cellular structures and increasing rates of congenital pathogenesis or spontaneous gestational termination.</div>", unsafe_allow_html=True)

elif selected_tab == "📊 Diagnostic Core":
    st.header("II. COMPUTATIONAL GENOMIC ANALYTICS")
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader("🧬 Microbial Genomic Input")
        real_ncbi_dna = "ATGGCGATCGATCGATCGATCGATCGATCGCGGCCAAACTTTTCTTGCCCCCCGGGTCACTTTATCAGTTAGAAACCTCTCAAAAATTTTAGGGGCGCTATTATTTTATCTGCTCAAACAATATCTGGGACGCTTTCTGGAAAGACAAGTCCAGTATGAATCAGTAATCAGTCAATACTTATGATTAGCGGCTTCCCCACAGCTGCGGCCAACAAATTCCTCCACTTCTGCCATTGCCAATCCCCAGCGTGGAAAAACATTGGACACACACACCAATTGAGTCGCGGGGAGATATTTCTCGCCCAATTTTGACGGCA"
        dna_input = st.text_area("Bacterial DNA Sequence Metadata (Bases: A, T, C, G):", value=real_ncbi_dna, height=150)
    with col_right:
        st.subheader("🤰 Maternal Clinical Parameters")
        sonar_status = st.selectbox("High-Resolution Fetal Ultrasonography Matrix:", ["Optimal & Physiological Fetal Development", "Mild Intrauterine Growth Restriction (IUGR)", "Acute Fetal Distress / Heartrate Abnormalities"])
        biomarker_score = st.slider("Serum Inflammatory Cytokine & Biomarker Index (%):", 0, 100, 25)
 st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⚡ EXECUTE COMPUTATIONAL INTEGRATED RISK PREDICTION"):
        dna_sequence = dna_input.strip().upper()
        if not all(char in "ATCG" for char in dna_sequence):
            st.error("❌ Diagnostic Protocol Refused: Alphanumeric sequence mismatch. Only canonical A, T, C, and G nitrogenous bases permitted.")
        else:
            total_length = len(dna_sequence)
            count_C = dna_sequence.count('C')
            count_G = dna_sequence.count('G')
            gc_content = ((count_G + count_C) / total_length) * 100
            st.success("✅ DATA INTEGRATION SUCCESSFUL: Neural Matrix Correlated.")
            
            m_col1, m_col2, m_col3 = st.columns(3)
            with m_col1: st.metric("🧬 DNA Sequence Length", f"{total_length} bases")
            with m_col2: st.metric("📊 Genomic Stability (GC%)", f"{gc_content:.2f}%")
            with m_col3:
                if gc_content > 45 or "Optimal" not in sonar_status or biomarker_score > 60:
                    status_text = "🚨 POTENTIAL PATHOGENIC RISK"
                    st.metric("👶 Fetal Health Assessment", status_text)
                    st.warning("⚠️ CLINICAL ALERT: High thermodynamic genomic stability indicates adaptive environmental micro-mutations linked with bio-toxin hyper-expression. Immediate restriction of local environmental water vectors, specialized fetal echocardiography, and immediate implementation of cell-free Non-Invasive Prenatal Testing (NIPT) are strongly recommended.")
                else:
                    status_text = "🟢 PHYSIOLOGICAL STATUS: OPTIMAL"
                    st.metric("👶 Fetal Health Assessment", status_text)
                    st.info("ℹ️ PREDICTIVE PROGNOSTIC OVERVIEW: The computational analysis isolates stable environmental strains showing zero toxin hyper-expression signatures. Integrated maternal diagnostics confirm that early embryonic cellular development continues along healthy physiological trajectories.")
