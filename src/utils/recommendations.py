def generate_recommendations(weather, soil_type, fertilizer, cultivation_method):
    recommendations = []

    # Weather recommendations
    if weather['temperature'] > 30:
        recommendations.append(
            "Cân nhắc sử dụng lưới che để bảo vệ cây trồng khỏi nhiệt độ quá cao.")
    if weather['humidity'] < 40:
        recommendations.append("Có thể cần tưới tiêu do độ ẩm thấp.")

    # Soil type recommendations
    if soil_type == "Cát":
        recommendations.append(
            "Cân nhắc thêm chất hữu cơ để cải thiện độ phì nhiêu của đất.")
    elif soil_type == "Sét":
        recommendations.append("Đảm bảo thoát nước tốt để tránh ngập úng.")
    elif soil_type == "Thịt":
        recommendations.append(
            "Loại đất này giữ ẩm tốt; cần theo dõi để tránh tưới quá nhiều.")
    elif soil_type == "Mùn":
        recommendations.append(
            "Đất này giàu dinh dưỡng; nên kiểm tra định kỳ.")

    # Fertilizer recommendations
    if fertilizer == "Hữu cơ":
        recommendations.append(
            "Phân bón hữu cơ có thể cải thiện sức khỏe đất theo thời gian.")
    elif fertilizer == "Vô cơ":
        recommendations.append(
            "Đảm bảo bón phân cân đối để tránh làm cạn kiệt đất.")
    elif fertilizer == "Vi sinh":
        recommendations.append(
            "Phân bón vi sinh có thể tăng cường hấp thu dinh dưỡng.")

    # Cultivation method recommendations
    if cultivation_method == "Thủy canh":
        recommendations.append(
            "Theo dõi chặt chẽ mức dinh dưỡng để cây phát triển tối ưu.")
    elif cultivation_method == "Khí canh":
        recommendations.append(
            "Đảm bảo khoảng thời gian phun sương hợp lý để duy trì độ ẩm.")
    elif cultivation_method == "Công nghệ cao":
        recommendations.append(
            "Sử dụng các công cụ nông nghiệp chính xác để quản lý năng suất tốt hơn.")
    elif cultivation_method == "Truyền thống":
        recommendations.append(
            "Cân nhắc luân canh cây trồng để duy trì sức khỏe đất.")
    return recommendations
