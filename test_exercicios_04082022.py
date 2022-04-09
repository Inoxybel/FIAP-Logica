import unittest

from exercicios import *

# Teste das APIs criadas no modulo exercicios.py
class TestExercicios(unittest.TestCase):
 
    def test_validaNotas(self):
        self.assertEqual(validaNotas([1, 2, 3]), 0)
        self.assertEqual(validaNotas([1, 2, -3]), 3)
        self.assertEqual(validaNotas([1, 22, 3]), 2)
        self.assertEqual(validaNotas([0, 2, 3]), 0)

    def test_excluiMenorNota(self):
        self.assertEqual(excluiMenorNota([1, 2, 3]), [2, 3])
        self.assertEqual(excluiMenorNota([3, 2, 1]), [3, 2])
        self.assertEqual(excluiMenorNota([1, 3, 2]), [3, 2])
        self.assertEqual(excluiMenorNota([2, 3, 1]), [2, 3])
        self.assertEqual(excluiMenorNota([3, 1, 2]), [3, 2])
        self.assertEqual(excluiMenorNota([2, 1, 3]), [2, 3])

    def test_calculaMedia(self):
        self.assertEqual(calculaMedia([10, 10, 10]), 10)
        self.assertEqual(calculaMedia([6.5, 7.5]), 7.0)
        self.assertEqual(calculaMedia([4.5, 3.5]), 4.0)

if __name__ == "__main__":
    unittest.main()

