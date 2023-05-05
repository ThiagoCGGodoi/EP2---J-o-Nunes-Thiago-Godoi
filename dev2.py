def posiciona_frota(dicio):
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

armada = {}
navios_possiveis = {'porta-aviões': [4,1], 'navio-tanque': [3,2], 'contratorpedeiro': [2,3], 'submarino': [1,4]}
for navio, infos in navios_possiveis.items():
  nome = navio
  tamanho = infos[0]
  quantidade = infos[1]
  for i in range(0, quantidade):
    verificado = False
    while verificado == False:
      print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, infos[0]))
      linha = input('Escolha a linha: ')
      coluna = input('Escolha uma coluna: ')
      if linha == '' or coluna == '':
        print('Esta posição não está válida!')
      else:
        linha = int(linha)
        coluna = int(coluna)
        if nome != 'submarino':
          orientacao_inp = int(input('Digite 1 para orientação vertical ou 2 para horizontal: '))
          if orientacao_inp == 1:
            orientacao = 'vertical'
          else:
            orientacao = 'horizontal'
          verificado = posicao_valida(armada, linha, coluna, orientacao, tamanho)
          if verificado == False:
            print('Esta posição não está válida!')
          else:
            posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)
            armada = preenche_frota(armada, navio, linha, coluna, orientacao, tamanho)
            verificado = True
        else:
          orientacao = 'vertical'
          verificado = posicao_valida(armada, linha, coluna, orientacao, tamanho)
          if verificado == False:
            print('Esta posição não está válida!')
          else:
            posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)
            armada = preenche_frota(armada, navio, linha, coluna, orientacao, tamanho)
            verificado = True
print(armada)