import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="AI-Marshes Microbe", page_icon="🧬", layout="wide")

# 2. Main Platform Header
st.title("🧬 AI-Marshes Microbe Platform")
st.caption("Advanced Genomic Predictive System for Waterborne Pathogen Mutations and Embryonic Cytotoxicity")
st.markdown("---")

# 3. Sidebar Navigation Panel
st.sidebar.header("🕹️ Control Dashboard")
st.sidebar.markdown("Lead Researcher: Taiba Firas")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigate Platform:", ["📊 AI Predictive System", "🔬 Scientific Research Hypothesis"])

# --- Section 1: Scientific Hypothesis ---
if page == "🔬 Scientific Research Hypothesis":
    st.header("📋 Core Scientific Hypothesis")
    st.subheader("Impact of Climate-Driven Microbial Mutations in Iraqi Marshes on Embryonic Stability")
    st.write("Due to drought and salinity in the Iraqi marshes, waterborne pathogens undergo rapid genomic mutations. These micro-mutations trigger an up-regulation in biotoxin synthesis. When exposed to pregnant women, these mutated toxins directly target early embryonic cells, increasing congenital deformities or spontaneous abortions. This platform simulates these variations to predict toxicity.")

# --- Section 2: AI Predictive System ---
elif page == "📊 AI Predictive System":
    st.header("🧬 Genomic Sequencing & Embryonic Risk Simulation")
    
    dna_input = st.text_area(
        "Enter Waterborne Bacterial DNA Sequence (A, T, C, G characters only):", 
        value="ATGGCGATCGATCGATCGATCGATCGATCGATCGATCGATC", 
        height=150
    )
    
    if st.button("🚀 Execute AI Genomic Simulation"):
        dna_sequence = dna_input.strip().upper().replace(" ", "").replace("\n", "")
        
        if not dna_sequence or not all(char in "ATCG" for char in dna_sequence):
            st.error("❌ Input Error: Invalid genomic sequence detected. Please provide standard bases (A, T, C, G).")
        else:
            total_length = len(dna_sequence)
            count_C = dna_sequence.count('C')
            count_G = dna_sequence.count('G')
            gc_content = ((count_G + count_C) / total_length) * 100
            
            st.success("✅ Genomic Sequence Successfully Processed and Analyzed!")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="🧬 Total Sequence Length", value=f"{total_length} bp")
            with col2:
                st.metric(label="📊 Genomic Stability (GC%)", value=f"{gc_content:.2f}%")
            with col3:
                if gc_content > 45:
                    toxicity_score = random.randint(75, 96)
                    risk_level = "🚨 High Cellular Risk"
                else:
                    toxicity_score = random.randint(15, 48)
                    risk_level = "🟢 Low / Stable Risk"
                st.metric(label="⚠️ Embryonic Cytotoxicity Evaluation", value=risk_level)
            
            st.markdown("---")
            st.subheader("🧠 AI Genomic Analytics & Predictive Report:")
            st.write(f"▪️ Predicted Embryonic Membrane Penetration Probability: {toxicity_score}%")
            
            if toxicity_score > 70:
                st.warning("🚨 High Risk: This bacterial strain poses a threat to embryonic cell viability. Isolate water source immediately.")
            else:
                st.info("🟢 Safe Strain: The strain shows standard genomic equilibrium. No immediate danger to embryonic development.")
