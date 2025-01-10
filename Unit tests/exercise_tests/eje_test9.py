from ejercicio import even_numbers
import unittest

class TestEvenNumbers(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = even_numbers([1, 8, 3, 6, 12, 5])
        
    def test_1(self):        
        self.assertEqual([8, 6, 12], resultado)

    def test_2(self):
        self.assertNotEqual([2,3,5], resultado)

    def test_3(self):
        self.assertIsNotNone(resultado)

    def test_4(self):
        self.assertIsNot([8, 6, 12], resultado)

    def test_5(self):
        self.assertIn(12, resultado)

    def test_6(self):
        self.assertNotIn(5,resultado)

if __name__ == '__main__':
    unittest.main()