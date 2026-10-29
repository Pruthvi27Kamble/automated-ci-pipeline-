# Core Application Engine
def calculate_grade(marks)
    if not isinstance(marks, (int, float)):
        raise TypeError("Marks must be a numeric value")
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
        
    if marks >= 90: return "A"
    elif marks >= 75: return "B"
    elif marks >= 60: return "C"
    else: return "Fail"
