import streamlit as st
import joblib
import numpy as np
import time

# Set the page configuration for a wide layout
st.set_page_config(layout="wide", page_title="Prediction|Churn prediction MLWA", page_icon="🎰")

# Correct the file paths to be relative to the project root
# This is crucial for a multipage app structure
try:
    scaler = joblib.load("pages/scaler.pkl")
    model = joblib.load("pages/model.pkl")
except FileNotFoundError:
    st.error("Error: Model files (scaler.pkl or model.pkl) not found. Please ensure they are in the 'pages' directory.")
    st.stop()

st.title("🔮 Churn Prediction")
st.markdown("Enter the customer's details below and hit 'Predict' to see the result.")

st.divider()

# Use columns for a cleaner, more organized input form
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, value=30, help="Enter the customer's age.")
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=130, value=10, help="How many months the customer has been with the company.")

with col2:
    monthlycharge = st.number_input("Monthly Charge ($)", min_value=30.0, max_value=150.0, value=50.0, help="The customer's average monthly bill.")
    gender = st.selectbox("Gender", ["Male", "Female"], help="Select the customer's gender.")

st.divider()

# Prediction button
predict_button = st.button("Predict Churn", use_container_width=True, type="primary")

# --- Prediction Logic and Animated Result ---
if predict_button:
    # Prepare the input data
    gender_selected = 1 if gender.lower() == "female" else 0
    X = np.array([[age, gender_selected, tenure, monthlycharge]])

    # Use an animated success/warning message
    with st.spinner("Analyzing data..."):
        time.sleep(1) # Simulate a brief processing delay

    # Scale the input and make the prediction
    try:
        X_scaled = scaler.transform(X)
        prediction = model.predict(X_scaled)[0]

        if prediction == 1:
            st.error("🔴 Prediction: This customer is likely to **CHURN**!", icon="❗")
        else:
            st.success("🟢 Prediction: This customer is **NOT** likely to churn.", icon="✅")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
