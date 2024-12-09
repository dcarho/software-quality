from ejercicio import max
import unittest

class TestMax(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = max([1, 8, 3, 0, 12])
        
    def test_1(self):        
        self.assertEqual(12, resultado)

    def test_2(self):
        self.assertNotEqual(8, resultado)

    def test_3(self):
        self.assertIsNotNone(resultado)

    def test_4(self):
        self.assertIs(12, resultado)

    def test_5(self):
        self.assertTrue(resultado == 12)

    def test_6(self):
        self.assertFalse(resultado != 12)

if __name__ == '__main__':
    unittest.main()