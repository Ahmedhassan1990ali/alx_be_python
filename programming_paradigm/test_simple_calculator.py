import unittest
from simple_calculator import SimpleCalculator

class Test_simple_calculato(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2,3),-1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,3),6)

    def test_division(self):
        self.assertEqual(self.calc.divide(6,3),2)
        self.assertEqual(self.calc.divide(6,0),None)
    