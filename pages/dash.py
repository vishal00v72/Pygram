import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration for a wide layout and a professional look
st.set_page_config(
    page_title="Dashboard",
    page_icon="🎰",
    layout="wide"
)

# --- 1. Load Data ---
@st.cache_data
def load_data():
    
    try:
        # Corrected file path to 'pages/customer_churn_data.csv'
        df = pd.read_csv("pages/customer_churn_data.csv")
        return df
    except FileNotFoundError:
        st.error("Dataset file 'pages/customer_churn_data.csv' not found. Please ensure it's in the 'pages' directory.")
        return None

# Load the resources
df = load_data()

# --- 2. Title and Description ---
st.title("📊 Customer Churn Data Visualization Dashboard")
st.markdown("This dashboard provides an interactive overview of key trends and relationships within the customer churn dataset.")
st.divider()

# --- 3. Data Visualization (Main Content) ---
st.header("Dataset Insights & Visualizations")

if df is not None:
    tab1, tab2, tab3, tab4 = st.tabs(["Distributions", "Relationships", "Correlations", "Categorical Analysis"])

    # Tab 1: Distributions
    with tab1:
        st.subheader("Distribution of Key Features")
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### Monthly Charges Distribution")
            st.bar_chart(df['MonthlyCharges'])
        with col2:
            st.write("#### Tenure Distribution")
            st.bar_chart(df['Tenure'])
    
    # Tab 2: Relationships
    with tab2:
        st.subheader("Relationships Between Features")
        st.write("#### Tenure vs. Monthly Charges (Colored by Churn)")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='Tenure', y='MonthlyCharges', hue='Churn', data=df, ax=ax)
        st.pyplot(fig)

    # Tab 3: Correlations
    with tab3:
        st.subheader("Feature Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 8))
        numeric_df = df.select_dtypes(include=np.number)
        sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    # Tab 4: Categorical Analysis (New visualizations)
    with tab4:
        st.subheader("Categorical Feature Insights")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("#### Churn Rate by Contract Type")
            contract_churn = df.groupby('ContractType')['Churn'].value_counts(normalize=True).unstack().fillna(0)
            st.bar_chart(contract_churn)
            
        with col2:
            st.write("#### Churn Rate by Internet Service")
            internet_churn = df.groupby('InternetService')['Churn'].value_counts(normalize=True).unstack().fillna(0)
            st.bar_chart(internet_churn)
else:
    st.info("Please ensure 'pages/customer_churn_data.csv' is in the correct directory for visualizations.")