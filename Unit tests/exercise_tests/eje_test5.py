from ejercicio import length
import unittest

class TestLength(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = length("Test")
        
    def test_1(self):        
        self.assertEqual("Less than 5", resultado)

    def test_2(self):
        self.assertNotEqual("Longer than 5", resultado)

    def test_3(self):
        self.assertIsNotNone(resultado)

    def test_4(self):
        self.assertIsNot("Longer than 5", resultado)

    def test_5(self):
        self.assertIn("Less",resultado)

    def test_6(self):
        self.assertNotIn("Longer",resultado)

if __name__ == '__main__':
    unittest.main()