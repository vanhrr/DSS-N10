import streamlit as st
import pandas as pd
# Tiêu đề ứng dụng
st.title("Nhập Dữ Liệu Canh Tác")

# Các trường nhập dữ liệu
temp = st.number_input("Nhiệt độ (°C)", min_value=-10.0, max_value=50.0, value=25.0)
humidity = st.number_input("Độ ẩm (%)", min_value=0, max_value=100, value=60)
rainfall = st.number_input("Lượng mưa (mm)", min_value=0.0, max_value=500.0, value=100.0)
soil_type = st.selectbox("Loại đất", ["Cát", "Sét", "Thịt", "Mùn"])
fertilizer = st.selectbox("Loại phân bón", ["Hữu cơ", "Vô cơ", "Vi sinh", "Không sử dụng"])
cultivation_method = st.selectbox(
    "Kỹ thuật canh tác", 
    ["Hữu cơ", "Thủy canh", "Khí canh", "Công nghệ cao", "Truyền thống"]
)

yield_estimate = st.number_input("Năng suất dự kiến (kg/ha)", min_value=0.0, max_value=10000.0, value=3000.0)
slider=st.slider('Chon 1 gia tri',1,2,3)

# Lưu dữ liệu nếu người dùng nhấn nút
# if st.button("Lưu dữ liệu"):
#     data = {
#         "Nhiệt độ (°C)": [temp],
#         "Độ ẩm (%)": [humidity],
#         "Lượng mưa (mm)": [rainfall],
#         "Loại đất": [soil_type],
#         "Loại phân bón": [fertilizer],
#         "Năng suất dự kiến (kg/ha)": [yield_estimate]
#     }
#     df = pd.DataFrame(data)
#     df.to_csv("crop_data.csv", mode='a', header=False, index=False)
#     st.success("Dữ liệu đã được lưu thành công!")
0
st.write(f'Temperature: {temp}')