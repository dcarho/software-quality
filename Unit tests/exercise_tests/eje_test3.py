from ejercicio import mult
import unittest

class TestMult(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = mult(3)
        
    def test_1(self):        
        self.assertEqual(24, resultado)

    def test_2(self):
        self.assertNotEqual(90, resultado)

    def test_3(self):
        self.assertTrue(resultado == 24)

    def test_4(self):
        self.assertFalse(resultado != 24)

if __name__ == '__main__':
    unittest.main()