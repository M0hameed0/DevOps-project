import unittest
from health_utils import calculate_bmi, calculate_bmr

# Définition d'une classe de tests unitaires pour les utilitaires de calcul de santé
class TestHealthCalculatorUtils(unittest.TestCase):

    # Test pour la fonction calculate_bmi
    def test_calculate_bmi(self):
        # Vérifie que le calcul de l'IMC est correct pour un poids de 70 kg et une taille de 1.75 m
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)
        # Vérifie que la fonction lève une erreur si le poids est négatif
        with self.assertRaises(ValueError):
            calculate_bmi(-70, 1.75)
    # Test pour la fonction calculate_bmr pour un homme
    def test_calculate_bmr_male(self):
        # Vérifie que le calcul du BMR pour un homme est correct avec des données données
        self.assertEqual(calculate_bmr(70, 175, 30, 'male'), 1695.67)

    # Test pour la fonction calculate_bmr pour une femme
    def test_calculate_bmr_female(self):
        # Vérifie que le calcul du BMR pour une femme est correct avec des données données
        self.assertEqual(calculate_bmr(70, 175, 30, 'female'), 1507.13)
        
    # Test pour la fonction calculate_bmr avec une entrée de sexe invalide
    def test_calculate_bmr_invalid(self):
        # Vérifie que la fonction lève une erreur si une valeur de sexe invalide est fournie
        with self.assertRaises(ValueError):
            calculate_bmr(70, 175, 30, 'other')

# Point d'entrée du script, lance les tests si le fichier est exécuté directement
if __name__ == '__main__':
    unittest.main()
