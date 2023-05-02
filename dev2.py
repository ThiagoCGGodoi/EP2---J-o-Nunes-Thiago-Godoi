def posiciona_frota(dicio):
  '''tabuleiro = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10]'''
  for tipo_navio in dicio.values():
    for navio in tipo_navio:
      for coordenada in navio:
        x = coordenada[0]
        y = coordenada[1]
        tabuleiro[x][y] = 1
  return tabuleiro