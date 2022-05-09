from random import randrange


def preenche_posicao_tabuleiro(tabuleiro):
    i = randrange(8)
    j = randrange(8)

    if tabuleiro[i][j] == 1:
        preenche_posicao_tabuleiro(tabuleiro)
    else:
        tabuleiro[i][j] = 1

    return tabuleiro

def preenche_tabuleiro(tabuleiro):
    for i in range(8):
        tabuleiro = preenche_posicao_tabuleiro(tabuleiro)
    
    return tabuleiro
