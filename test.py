import unittest
from main import Kalkulacka

class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucet(1, 2), 3)

    def test_add_negative(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucet(1, 2), 3)

    def test_add_floats(self):
        calc = Kalkulacka()
        self.assertAlmostEqual(calc.sucet(1.1, 2.2), 3.3, places=1)

    def test_add_kvadraticka_rovnica(self):
        calc = Kalkulacka()
        self.assertEqual(calc.kvadraticka_rovnica(x1))

if __name__ == "__main__":
    unittest.main()
