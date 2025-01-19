import unittest
from simple_calculator import SimpleCalculator

class Test_simple_calculato(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calc .add(2,3),5)

    def test_subtract(self):
        self.assertEqual(self.calc .subtract(2,3),-1)

    def test_multiply(self):
        self.assertEqual(self.calc .multiply(2,3),6)

    def test_divide(self):
        self.assertEqual(self.calc .divide(6,3),2)
        self.assertEqual(self.calc .divide(6,0),None)
    