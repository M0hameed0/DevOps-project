from flask import Flask, render_template, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        # Récupérer les données du formulaire
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # Calculer le BMI
        bmi_result = calculate_bmi(weight, height)

        return jsonify({'bmi': bmi_result}), 200
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        # Récupérer les données du formulaire
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']

        # Calculer le BMR
        bmr_result = calculate_bmr(weight, height, age, gender)

        return jsonify({'bmr': bmr_result}), 200
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True)