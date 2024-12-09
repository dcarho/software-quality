from ejercicio import is_even
import unittest

class TestIsEven(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = is_even(23)
        
    def test_1(self):        
        self.assertEqual(False, resultado)

    def test_2(self):
        self.assertNotEqual(True, resultado)

    def test_3(self):
        self.assertIsNotNone(resultado)

    def test_4(self):
        self.assertIsNot(True, resultado)

    def test_5(self):
        self.assertTrue(not resultado)

    def test_6(self):
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()