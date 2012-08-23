import unittest
from boliche import *


class TestBoliche(unittest.TestCase):

    def test_calcula_jogada_sem_erro_strike_spare(self):
        jogada = "12345462"
        esperado = 27
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_com_erro_sem_strike_spare(self):
        jogada = "2453--"
        esperado = 14
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_sem_erro_sem_strike_com_um_spare(self):
        jogada = "14527/1"
        esperado = 23
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_com_erro_sem_strike_com_spare(self):
        jogada = "5472-/7"
        esperado = 35
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_sem_erro_com_strike_sem_spare(self):
        jogada = "81X2526"
        esperado = 41
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

if __name__ == '__main__':
    unittest.main()
