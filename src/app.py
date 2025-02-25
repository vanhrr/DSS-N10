import streamlit as st
import pandas as pd
import numpy as np
import joblib
from utils.recommendations import generate_recommendations

# Background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:url("https://images.pexels.com/photos/30733228/pexels-photo-30733228/free-photo-of-nong-nghi-p-truy-n-th-ng-canh-d-ng-thu-c-la-dong-java.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    #bd69ec75 {{
        color: white;
        front-size: 100px;
        
    }}
    p, li {{
        font-weight: 600;
        color: white;
    }}
    .e6rk8up3{{
            background-color: RGBA(0,0,0,0.3);
            padding: 30px;
            border-radius: 20px;
            width: 764px;
    }}
    .e1d5ycv52{{
            background-color: #bd69ec75;
            transition:1s;
    }}
    .e1d5ycv52:hover{{
            background-color: #bd69ec75;
            scale: 1.3;
    }}
    .stButton{{
            display: flex;
            justify-content: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# Load model and label encoders
model = joblib.load('./models/yield_model.pkl')
label_encoders = joblib.load('./models/yield_model_label_encoders.pkl')
feature_importances = joblib.load('./models/feature_importances.pkl')

data = pd.read_csv('./data/data_season_vietnamese.csv')

# Determine min and max values for each feature
min_values = data.min()
max_values = data.max()
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

    feature_names = ['rainfall', 'temp', 'soil_type',
                     'cultivation_method', 'fertilizer', 'humidity', 'tree_name']
    feature_names_vn = ['Lượng mưa', 'Nhiệt độ', 'Loại đất',
                        'Phương pháp canh tác', 'Phân bón', 'Độ ẩm', 'Loại cây']
    most_important_feature_index = np.argmax(feature_importances)
    most_important_feature = feature_names[most_important_feature_index]
    most_important_feature_vn = feature_names_vn[most_important_feature_index]

    # Test different values for the most important feature
    if most_important_feature in ['soil_type', 'cultivation_method', 'fertilizer', 'tree_name']:
        # Handle categorical features
        unique_values = data[most_important_feature].unique()
        test_values = label_encoders[most_important_feature].transform(
            unique_values)
    else:
        # Handle numeric features
        min_value = min_values[most_important_feature]
        max_value = max_values[most_important_feature]
        test_values = np.linspace(min_value, max_value, num=5)

    yield_estimates = []
    for value in test_values:
        test_data = input_data.copy()
        test_data[0, most_important_feature_index] = value
        yield_estimates.append(model.predict(test_data)[0])

    # Determine the best value for the most important feature
    best_value_index = np.argmax(yield_estimates)
    best_value = test_values[best_value_index]
    best_yield = yield_estimates[best_value_index]

    # Convert best_value to text if the feature is categorical
    if most_important_feature in ['soil_type', 'cultivation_method', 'fertilizer', 'tree_name']:
        best_value = label_encoders[most_important_feature].inverse_transform([
                                                                              int(best_value)])[0]
    # Generate and display recommendations
    recommendations = generate_recommendations({
        'temperature': temp,
        'humidity': humidity,
        'rainfall': rainfall
    }, soil_type, fertilizer, cultivation_method)

    st.write(
        f"Yếu tố quan trọng nhất để cải thiện năng suất: {most_important_feature_vn}")
    st.write(
        f"Giá trị hiện tại của {most_important_feature_vn}: {input_data[0, most_important_feature_index]}")
    st.write(
        f"Giá trị tốt nhất của {most_important_feature_vn} để cải thiện năng suất: {best_value}")
    st.write(f"Năng suất dự đoán với giá trị tốt nhất: {best_yield:.2f} kg/ha")
    st.write("Khuyến nghị để cải thiện năng suất cây trồng của bạn:")
    for rec in recommendations:
        st.write(f"- {rec}")
