def generate_recommendations(weather, soil_type, fertilizer, cultivation_method):
    recommendations = []

    # Weather recommendations
    if weather['temperature'] > 30:
        recommendations.append("Consider using shade nets to protect crops from excessive heat.")
    if weather['humidity'] < 40:
        recommendations.append("Irrigation may be necessary due to low humidity levels.")
    
    # Soil type recommendations
    if soil_type == "Cát":
        recommendations.append("Consider adding organic matter to improve soil fertility.")
    elif soil_type == "Sét":
        recommendations.append("Ensure proper drainage to prevent waterlogging.")
    elif soil_type == "Thịt":
        recommendations.append("This soil type retains moisture well; monitor for overwatering.")
    elif soil_type == "Mùn":
        recommendations.append("This soil is nutrient-rich; regular testing is recommended.")

    # Fertilizer recommendations
    if fertilizer == "Hữu cơ":
        recommendations.append("Organic fertilizers can improve soil health over time.")
    elif fertilizer == "Vô cơ":
        recommendations.append("Ensure balanced nutrient application to avoid soil depletion.")
    elif fertilizer == "Vi sinh":
        recommendations.append("Microbial fertilizers can enhance nutrient uptake.")

    # Cultivation method recommendations
    if cultivation_method == "Thủy canh":
        recommendations.append("Monitor nutrient levels closely for optimal growth.")
    elif cultivation_method == "Khí canh":
        recommendations.append("Ensure proper misting intervals to maintain humidity.")
    elif cultivation_method == "Công nghệ cao":
        recommendations.append("Utilize precision agriculture tools for better yield management.")
    elif cultivation_method == "Truyền thống":
        recommendations.append("Consider crop rotation to maintain soil health.")

    return recommendations