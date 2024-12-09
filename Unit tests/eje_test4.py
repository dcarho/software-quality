from ejercicio import divide
import unittest

class TestDivide(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = divide(24,3)
        
    def test_1(self):        
        self.assertEqual(8, resultado)

    def test_2(self):
        self.assertNotEqual(80, resultado)

    def test_3(self):
        self.assertTrue(resultado == 8)

    def test_4(self):
        self.assertFalse(resultado != 8)

if __name__ == '__main__':
    unittest.main()