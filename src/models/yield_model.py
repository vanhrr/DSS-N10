import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import numpy as np

# Đọc dữ liệu từ file CSV
data = pd.read_csv('../data/data_season_vietnamese.csv')

# Xử lý dữ liệu
label_encoders = {}
for column in ['soil_type', 'cultivation_method', 'fertilizer', 'tree_name']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Chọn các cột đầu vào và đầu ra
X = data[['rainfall', 'temp', 'soil_type', 'cultivation_method',
          'fertilizer', 'humidity', 'tree_name']]
y = data['yield']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Lưu mô hình và label encoders
joblib.dump(model, './yield_model.pkl')
joblib.dump(label_encoders, './yield_model_label_encoders.pkl')

# Lưu feature importances dựa trên coefficients
feature_importances = np.abs(model.coef_)
joblib.dump(feature_importances, './feature_importances.pkl')

# Đánh giá mô hình
score = model.score(X_test, y_test)
print(f'Model R^2 score: {score}')
