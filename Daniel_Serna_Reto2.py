def calles(felipe, chandler, direcciones):
  puntajeChandler = 0
  puntajeFelipe = 0
  lista = []
  for i in range(len(direcciones)):
    if direcciones[i] in felipe:
      puntajeFelipe += 1
    if direcciones[i] in chandler:
      puntajeChandler += 1
    if puntajeChandler>puntajeFelipe:
      lista.append('C')
    elif puntajeChandler<puntajeFelipe:
      lista.append('F')
    else:
      lista.append('J')
  print(''.join(lista))
calles(input('Letras Felipe '),input('Letras Chandler '), input('Avenidas visitadas '))
    
