from flask import Flask, render_template, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

# Initialisation de l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route('/')
def home():
    # Retourne le fichier HTML 'home.html' comme page d'accueil
    return render_template('home.html')

# Définir la route pour le calcul du BMI (Body Mass Index)
@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        # Récupérer les données du formulaire
        weight = float(request.form['weight']) # Poids en kilogrammes
        height = float(request.form['height']) # Taille en mètres

        # Calculer le BMI en utilisant la fonction `calculate_bmi
        bmi_result = calculate_bmi(weight, height)

        # Retourner le résultat sous forme JSON avec un code HTTP 200 (succès)
        return jsonify({'bmi': bmi_result}), 200
    except (KeyError, ValueError) as e:
        # En cas d'erreur (ex. : données manquantes ou invalides), retourner une erreur JSON avec un code HTTP 400
        return jsonify({'error': str(e)}), 400

# Définir la route pour le calcul du BMR (Basal Metabolic Rate)
@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        # Récupérer les données du formulaire
        weight = float(request.form['weight']) # Poids en kilogrammes
        height = float(request.form['height']) # Taille en centimètres
        age = int(request.form['age']) # Âge en années
        gender = request.form['gender'] # Genre ('male' ou 'female')

        # Calculer le BMR en utilisant la fonction `calculate_bmr`
        bmr_result = calculate_bmr(weight, height, age, gender)
        
        # Retourner le résultat sous forme JSON avec un code HTTP 200 (succès)
        return jsonify({'bmr': bmr_result}), 200
    except (KeyError, ValueError) as e:
        # En cas d'erreur (ex. : données manquantes ou invalides), retourner une erreur JSON avec un code HTTP 400
        return jsonify({'error': str(e)}), 400

# Point d'entrée principal de l'application
if __name__ == '__main__':
    # Lance l'application Flask en mode debug pour faciliter le développement
    app.run(debug=True)
