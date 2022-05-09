from collections import namedtuple

from .get_diagonal_direita import get_diagonal_direita
from .get_diagonal_esquerda import get_diagonal_esquerda


def possui_rainha_linha(tabuleiro, linha):
    if 1 in tabuleiro[linha]:
        return True
    else:
        return False

def possui_rainha_coluna(tabuleiro, coluna):
    if 1 in tabuleiro[:,coluna]:
        return True
    else:
        return False

def possui_rainha_diagonal_esquerda(tabuleiro, i, j):
    if 1 in get_diagonal_esquerda(tabuleiro, i, j):
        return True
    else:
        return False

def possui_rainha_diagonal_direita(tabuleiro, i, j):
    if 1 in get_diagonal_direita(tabuleiro, i, j):
        return True
    else:
        return False

def quantidade_rainhas(raio_ataque):
    return len(list(filter(lambda x: x == 1, raio_ataque)))

def get_posicoes_seguras(tabuleiro):
    posicao_segura = namedtuple('posicao_segura', ['linha', 'coluna'])
    posicoes_seguras = []

    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 1:
                if quantidade_rainhas(tabuleiro[i]) <= 1 and \
                quantidade_rainhas(tabuleiro[:,j]) <= 1 and \
                quantidade_rainhas(get_diagonal_esquerda(tabuleiro, i, j)) <= 1 and \
                quantidade_rainhas(get_diagonal_direita(tabuleiro, i, j)) <= 1:
                    posicoes_seguras.append(posicao_segura(i, j))
            else:
                if not possui_rainha_linha(tabuleiro, i) and \
                not possui_rainha_coluna(tabuleiro, j) and \
                not possui_rainha_diagonal_esquerda(tabuleiro, i, j) and \
                not possui_rainha_diagonal_direita(tabuleiro, i, j):
                    posicoes_seguras.append(posicao_segura(i, j))
    return posicoes_seguras


def organiza_tabuleiro(tabuleiro):
    posicoes_seguras = get_posicoes_seguras(tabuleiro)

    # Depois de pegar as posições seguras precisamos mover as rainhas
    # até que todas estejam em posições seguras.
    # Sempre que uma rainha se move as posições seguras devem ser atualizadas.
    pass
