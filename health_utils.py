def calculate_bmi(weight, height):
    """Calcule le Body Mass Index (BMI)."""
    if height <= 0 or weight <= 0:
        # Vérifie si les entrées sont valides (positives)
        raise ValueError("Height and weight must be positive values.")
    # Formule du BMI : poids / (taille^2), arrondi à 2 décimales
    return round(weight / (height ** 2), 2)

def calculate_bmr(weight, height, age, gender):
    """Calcule le Basal Metabolic Rate (BMR)."""
    # Vérifie si les entrées sont valides
    if any(value <= 0 for value in [weight, height, age]) or gender not in ['male', 'female']:
        raise ValueError("Invalid input values.")

    # Calcul spécifique selon le genre
    if gender == 'male':
        # Formule pour les hommes
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # gender == 'female'
        # Formule pour les femmes
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        
    # Retourne le BMR arrondi à 2 décimales
    return round(bmr, 2)
