import streamlit as st
import pandas as pd
from openai import OpenAI

# Set page config
st.set_page_config(page_title="RevGuard", layout="wide")

# Sidebar for API key and upload
with st.sidebar:
    st.title("RevGuard Setup")
    api_key = st.text_input("OpenAI API Key", type="password")
    uploaded_file = st.file_uploader("Upload Financial CSV", type=["csv"])

# Initialize OpenAI client
client = None
if api_key:
    client = OpenAI(sk-proj-uhyizaPvnrC7TrUnW-ogSHSOs8K)

# Main app
st.title("RevGuard AI Financial Analysis")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    if client and st.button("Analyze with AI"):
        # Prepare data sample for LLM
        sample_data = df.head(100).to_string()
        prompt = f"""
        Analyze this financial data and provide:
        1. Total income (sum of all positive amounts)
        2. Total expenses (sum of all negative amounts)
        3. Any unusual charges (unexpected or large negative amounts)
        4. Missed revenue opportunities (patterns suggesting lost revenue)
        5. General financial insights and recommendations

        Data sample:
        {sample_data}

        Provide response in markdown format with clear sections.
        """
        
        with st.spinner("AI is analyzing your finances..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )
                
                analysis = response.choices[0].message.content
                st.subheader("AI Financial Analysis")
                st.markdown(analysis)
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
else:
    st.info("Please upload a CSV file to get started")
