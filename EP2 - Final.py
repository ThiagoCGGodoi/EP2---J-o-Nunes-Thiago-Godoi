import random
random.seed(2)
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(0,tamanho):
            posicoes.append([linha+i, coluna])
    if orientacao == 'horizontal':
        for i in range(0,tamanho):
            posicoes.append([linha, coluna+i])
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

def posiciona_frota(dicio):
  tabuleiro = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
  for tipo_navio in dicio.values():
    for navio in tipo_navio:
      for coordenada in navio:
        x = coordenada[0]
        y = coordenada[1]
        tabuleiro[x][y] = 1
  return tabuleiro

def afundados(frota, tabuleiro):
  afundados = 0
  for tipo_navio, quantidade in frota.items():
    if tipo_navio == 'porta-aviões':
      partes_totais = 4
    elif tipo_navio == 'navio-tanque':
      partes_totais = 3
    elif tipo_navio == 'contratorpedeiro':
      partes_totais = 2
    else:
      partes_totais = 1
    for navio in quantidade:
      partes_afundadas = 0
      for coordenada in navio:
        x = coordenada[0]
        y = coordenada[1]
        if tabuleiro[x][y] == 'X':
          partes_afundadas += 1
        if partes_afundadas == partes_totais:
          afundados += 1
  return afundados

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

armada_jogador = {}
navios_possiveis = {'porta-aviões': [4,1], 'navio-tanque': [3,2], 'contratorpedeiro': [2,3], 'submarino': [1,4]}
for navio, infos in navios_possiveis.items():
  nome = navio
  tamanho = infos[0]
  quantidade = infos[1]
  for i in range(0, quantidade):
    verificado = False
    while verificado == False:
      print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, infos[0]))
      linha = int(input('Escolha a linha: '))
      coluna = int(input('Escolha uma coluna: '))
      if nome != 'submarino':
        orientacao_inp = int(input('Digite 1 para orientação vertical ou 2 para horizontal: '))
        if orientacao_inp == 1:
          orientacao = 'vertical'
        else:
          orientacao = 'horizontal'
        verificado = posicao_valida(armada_jogador, linha, coluna, orientacao, tamanho)
        if verificado == False:
          print('Esta posição não está válida!')
        else:
          posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)
          armada_jogador = preenche_frota(armada_jogador, navio, linha, coluna, orientacao, tamanho)
          verificado = True
      else:
        orientacao = 'vertical'
        verificado = posicao_valida(armada_jogador, linha, coluna, orientacao, tamanho)
        if verificado == False:
          print('Esta posição não está válida!')
        else:
          posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)
          armada_jogador = preenche_frota(armada_jogador, navio, linha, coluna, orientacao, tamanho)
          verificado = True
armada_oponente = {
    'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'navio-tanque': [[[6, 0], [6, 1], [6, 2]],[[4, 3], [5, 3], [6, 3]]],
    'contratorpedeiro': [[[1, 6], [1, 7]],[[0, 5], [1, 5]],[[3, 6], [3, 7]]],
    'submarino': [[[2, 7]],[[0, 6]],[[9, 7]],[[7, 6]]]}

tabuleiro_jogador = posiciona_frota(armada_jogador)
tabuleiro_oponente = posiciona_frota(armada_oponente)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

jogando = True
lista_posicoes_oponente =[]
posicoes_ja_usadas = []
while jogando:
   print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))
   verificado = False
   while verificado == False:
    posicao_at = []
    linha = int(input('Jogador, escolha sua linha: '))
    if linha <= 9 and linha >= 0:
      posicao_at.append(linha)
      verificado = True
    else:
      print('Linha inválida!')
    coluna = int(input('Jogador, escolha sua coluna: '))
    if coluna <= 9 and coluna >= 0:
      posicao_at.append(coluna)
      verificado = True
    else:
      print('Coluna inválida!')
    if posicao_at in posicoes_ja_usadas:
      print('A posição linha LINHA e coluna COLUNA já foi informada anteriormente!')
    else:
      posicoes_ja_usadas.append(posicao_at)
      verificado = True
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    navios_abatidos = afundados(armada_oponente, tabuleiro_oponente)
    if navios_abatidos == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
       oponente_sorteio = True
       while oponente_sorteio:
        posicoes_op = []
        jogada_oponente_linha = random.randint(0, 9)
        posicoes_op.append(jogada_oponente_linha)
        jogada_oponente_coluna = random.randint(0, 9)
        posicoes_op.append(jogada_oponente_coluna)
        if posicoes_op not in lista_posicoes_oponente:
          lista_posicoes_oponente.append(posicoes_op)
          oponente_sorteio = False
    tabuleiro_jogador = faz_jogada(tabuleiro_jogador, jogada_oponente_linha, jogada_oponente_coluna)
    print(f"Seu oponente está atacando na linha {jogada_oponente_linha} e coluna {jogada_oponente_coluna}")
    nvaios_abatido_jogador = afundados(armada_jogador, tabuleiro_jogador)
    if nvaios_abatido_jogador == 10:
        print("Xi! O oponente derrubou toda a sua frota =(")
        jogando=False