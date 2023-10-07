from Mes_01.Semana_01.dia01_jogo_adivinhacao import jogo_adivinhacao
import pytest
from unittest.mock import patch

def test_jogo_adivinhacao_acertou():
    with patch('Mes_01.Semana_01.dia01_jogo_adivinhacao.random.randint', return_value=42):
        with patch('builtins.input', return_value='42'):
            assert jogo_adivinhacao(42) == 'Parabéns você acertou'

def test_jogo_adivinhacao_numero_maior_que_50():
    with patch('builtins.input', return_value='60'):
        assert jogo_adivinhacao(60) == 'Favor escolher um número entre 1 e 50'

def test_jogo_adivinhacao_numero_menor_que_1():
    with patch('builtins.input', return_value='-5'):
        assert jogo_adivinhacao(-5) == 'Favor escolher um número entre 1 e 50'

def test_jogo_adivinhacao_errado():
    with patch('Mes_01.Semana_01.dia01_jogo_adivinhacao.random.randint', return_value=42):
        with patch('builtins.input', return_value='24'):
            assert jogo_adivinhacao(24) == 'Você errou, o número era 42 e você escolheu 24'

def test_jogo_adivinhacao_acertou_primeira_tentativa():
    with patch('Mes_01.Semana_01.dia01_jogo_adivinhacao.random.randint', return_value=10):
        with patch('builtins.input', return_value='10'):
            assert jogo_adivinhacao(10) == 'Parabéns você acertou'
