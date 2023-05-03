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
    print(tipo_navio)
    if tipo_navio == 'porta-aviões':
      partes_totais = 4
    elif tipo_navio == 'navio-tanque':
      partes_totais = 3
    elif tipo_navio == 'contratorpedeiro':
      partes_totais = 2
    else:
      partes_totais = 1
    print(partes_totais)
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