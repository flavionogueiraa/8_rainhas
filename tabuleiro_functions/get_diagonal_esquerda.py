def get_diagonal_esquerda_superior(tabuleiro, i, j):
    diagonal = []
    while(0 <= i < 8 and 0 <= j < 8):
        # if i < 0:
        #     i = 0
        # if j < 0:
        #     j = 0
        
        diagonal.insert(0, tabuleiro[i][j])
        i -= 1
        j -= 1

    return diagonal

def get_diagonal_esquerda_inferior(tabuleiro, i, j):
    diagonal = []
    while(0 <= i < 8 and 0 <= j < 8):
        # if i > 7:
        #     i = 7
        # if j > 7:
        #     j = 7
        
        diagonal.append(tabuleiro[i][j])
        i += 1
        j += 1
    
    return diagonal

def get_diagonal_esquerda(tabuleiro, i, j):
    diagonal_esquerda = get_diagonal_esquerda_superior(tabuleiro, i, j)
    diagonal_esquerda += get_diagonal_esquerda_inferior(tabuleiro, i, j)
    return diagonal_esquerda
