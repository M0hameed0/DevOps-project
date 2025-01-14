import unittest
from health_utils import calculate_bmi, calculate_bmr
class TestHealthCalculatorUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)
        with self.assertRaises(ValueError):
            calculate_bmi(-70, 1.75)

    def test_calculate_bmr_male(self):
        self.assertEqual(calculate_bmr(70, 175, 30, 'male'), 1695.67)

    def test_calculate_bmr_female(self):
        self.assertEqual(calculate_bmr(70, 175, 30, 'female'), 1507.13)

    def test_calculate_bmr_invalid(self):
        with self.assertRaises(ValueError):
            calculate_bmr(70, 175, 30, 'other')

if __name__ == '__main__':
    unittest.main()