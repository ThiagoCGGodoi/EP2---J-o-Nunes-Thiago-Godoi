def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(0,tamanho):
            posicoes.append([linha+i, coluna])
    if orientacao == 'horizontal':
        for i in range(0,tamanho):
            posicoes.append([linha,coluna+i])
    return posicoes
def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    if len(frota) == 0:
            frota[nome] = [define_posicoes(linha, coluna, orientacao, tamanho)]
            return frota
    for variavel1, variavel2 in frota.items():
        if nome not in frota:
            frota[nome] = [define_posicoes(linha, coluna, orientacao, tamanho)]
            return frota
        elif nome == variavel1:
            variavel2.append(define_posicoes(linha, coluna, orientacao, tamanho))
    return frota
    