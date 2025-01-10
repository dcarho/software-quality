from ejercicio import remove_letter
import unittest

class TestRemoveLetter(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = remove_letter("t", "Hello test")
        
    def test_1(self):        
        self.assertEqual("Hello es", resultado)

    def test_2(self):
        self.assertNotEqual("Hello test", resultado)

    def test_3(self):
        self.assertIsNotNone(resultado)

    def test_4(self):
        self.assertIsNot("Hello test", resultado)

    def test_5(self):
        self.assertIn("l",resultado)

    def test_6(self):
        self.assertNotIn("t",resultado)

if __name__ == '__main__':
    unittest.main()