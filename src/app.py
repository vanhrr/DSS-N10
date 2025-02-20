import streamlit as st
import pandas as pd
import numpy as np
import joblib
# from utils.recommendations import generate_recommendations

# Load model and label encoders
model = joblib.load('models/yield_model.pkl')
label_encoders = joblib.load('models/yield_model_label_encoders.pkl')

# Title of the application
st.title("Hệ hỗ trợ ra quyết định cho nông dân")

# User input for weather, soil type, fertilizer, and cultivation methods
temp = st.number_input("Nhiệt độ (°C)", min_value=-
                       10.0, max_value=50.0, value=25.0)
humidity = st.number_input("Độ ẩm (%)", min_value=0, max_value=100, value=60)
rainfall = st.number_input(
    "Lượng mưa (mm)", min_value=0.0, max_value=3000.0, value=100.0)
soil_type = st.selectbox("Loại đất", label_encoders['soil_type'].classes_)
fertilizer = st.selectbox(
    "Loại phân bón", label_encoders['fertilizer'].classes_)
cultivation_method = st.selectbox(
    "Phương pháp canh tác", label_encoders['cultivation_method'].classes_)
tree_name = st.selectbox("Loại cây", label_encoders['tree_name'].classes_)

# Encode categorical inputs
soil_type_encoded = label_encoders['soil_type'].transform([soil_type])[0]
fertilizer_encoded = label_encoders['fertilizer'].transform([fertilizer])[0]
cultivation_method_encoded = label_encoders['cultivation_method'].transform([
                                                                            cultivation_method])[0]
tree_name_encoded = label_encoders['tree_name'].transform([tree_name])[0]

# Prepare input data for prediction
input_data = np.array([[rainfall, temp, soil_type_encoded,
                      cultivation_method_encoded, fertilizer_encoded, humidity, tree_name_encoded]])

# Make prediction
yield_estimate = model.predict(input_data)


if st.button('Dự đoán năng suất'):
    st.write(f"Dự đoán năng suất: {yield_estimate[0]:.2f} kg/ha")


# # Generate and display recommendations
# recommendations = generate_recommendations(
#     temp, humidity, rainfall, soil_type, fertilizer, cultivation_method, tree_name)
# st.write("Recommendations for Improving Yield:")
# for rec in recommendations:
#     st.write(f"- {rec}")
