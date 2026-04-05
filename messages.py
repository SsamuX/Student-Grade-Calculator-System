def get_performance_message(grade):
    if grade == "A":
        return "Excellent performance!"
    elif grade == "B":
        return "Very good performance!"
    elif grade == "C":
        return "Good performance!"
    elif grade == "D":
        return "Fair performance. Improve more."
    else:
        return "Poor performance. Work harder."
