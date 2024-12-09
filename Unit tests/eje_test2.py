from ejercicio import addit
import unittest

class TestAddit(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = addit(3)
        
    def test_1(self):        
        self.assertEqual(8, resultado)

    def test_2(self):
        self.assertNotEqual(9, resultado)

if __name__ == '__main__':
    unittest.main()