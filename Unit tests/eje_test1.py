from ejercicio import total
import unittest

class TestCalcularTotal(unittest.TestCase):
    
    def test_1(self):
        resultado = total([1, 2, 3 , 5])
        self.assertEqual(11, resultado)

if __name__ == '__main__':
    unittest.main()
