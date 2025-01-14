def calculate_bmi(weight, height):
    """Calcule le Body Mass Index (BMI)."""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")
    return round(weight / (height ** 2), 2)

def calculate_bmr(weight, height, age, gender):
    """Calcule le Basal Metabolic Rate (BMR)."""
    if any(value <= 0 for value in [weight, height, age]) or gender not in ['male', 'female']:
        raise ValueError("Invalid input values.")
    
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # gender == 'female'
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return round(bmr, 2)