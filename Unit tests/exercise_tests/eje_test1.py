from ejercicio import total
import unittest

class TestTotal(unittest.TestCase):
    
    def setUp(self):
        global resultado
        resultado = total([1, 2, 3 , 5])
    
    def test_1(self):
        
        self.assertEqual(11, resultado)
    
    def test_2(self):
       
        self.assertNotEqual(12, resultado)

if __name__ == '__main__':
    unittest.main()
