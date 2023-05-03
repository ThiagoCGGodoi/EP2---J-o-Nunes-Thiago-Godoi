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

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_a_validar = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao_a_validar in posicoes_a_validar:
        if posicao_a_validar[0] < 0 or posicao_a_validar[0] > 9 or posicao_a_validar[1] < 0 or posicao_a_validar[1] > 9:
            return False
        
    for posicoes_ja_ocupadas in frota.values():
        for posicoes in posicoes_ja_ocupadas:
            for posicao in posicoes:
                if posicao in posicoes_a_validar:
                    return False
   

    return True  