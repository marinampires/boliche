import unittest
from boliche import *


class TestBoliche(unittest.TestCase):

    def test_calcula_jogada_sem_erro_strike_spare(self):
        jogada = "12345462233223322332"
        esperado = 57
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_com_erro_sem_strike_spare(self):
        jogada = "9-9-9-9-9-9-9-9-9-9-"
        esperado = 90
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_sem_erro_sem_strike_com_um_spare(self):
        jogada = "5/5/5/5/5/5/5/5/5/5/5"
        esperado = 150
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_com_erro_sem_strike_com_spare(self):
        jogada = "547223322332233223-/7"
        esperado = 70
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_sem_erro_com_strike_sem_spare(self):
        jogada = "81X2526233223322332"
        esperado = 71
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

    def test_calcula_jogada_somente_com_strike(self):
        jogada = "XXXXXXXXXXXX"
        esperado = 300
        calculado = calcula(jogada)
        self.assertEquals(esperado, calculado)

if __name__ == '__main__':
    unittest.main()
