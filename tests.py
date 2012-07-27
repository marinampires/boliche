import unittest
from boliche import *


class TestBoliche(unittest.TestCase):
    def test_deve_acertar_todas_jogadas_sem_spare_ou_strike(self):
        jogada = ""
        esperado = 0
        for i in range(1, 11):
            jogada = jogada + "22"
            esperado = esperado + 4
        retorno = calcula(jogada)
        self.assertEqual(esperado, retorno)

if __name__ == '__main__':
    unittest.main()
