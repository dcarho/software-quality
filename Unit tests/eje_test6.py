from ejercicio import reverse
import unittest

class TestReverse(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = reverse("abc")
        
    def test_1(self):        
        self.assertEqual("cba", resultado)

    def test_2(self):
        self.assertNotEqual("abc", resultado)

    def test_3(self):
        self.assertIsNotNone(resultado)

    def test_4(self):
        self.assertIsNot("abc", resultado)

    def test_5(self):
        self.assertIn("b",resultado)

    def test_6(self):
        self.assertNotIn("s",resultado)

if __name__ == '__main__':
    unittest.main()