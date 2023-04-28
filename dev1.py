def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(0,tamanho):
            posicoes.append([linha+i, coluna])
    if orientacao == 'horizontal':
        for i in range(0,tamanho):
            posicoes.append([linha,coluna+i])
    return posicoes