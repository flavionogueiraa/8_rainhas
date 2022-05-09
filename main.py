
from tabuleiro_functions import (cria_tabuleiro, imprime_tabuleiro,
                                 organiza_tabuleiro, preenche_tabuleiro)

tabuleiro = cria_tabuleiro()
tabuleiro = preenche_tabuleiro(tabuleiro)
tabuleiro = organiza_tabuleiro(tabuleiro)

imprime_tabuleiro(tabuleiro)

# Criar tabuleiro - OK
# Criar rainhas - OK
# Preencher tabuleiro de forma aleatória - OK
# Organizar rainhas para não se atacarem
    # Saber quais posições são seguras
    # Saber se uma rainha está sendo atacada
    # Se sim, mudá-la para uma posição livre
        # Atualizar as posições seguras
    # Se não, continuar
