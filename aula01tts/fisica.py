print('Esse programa calcula a velocidade média de um patinete!')
distancia = float(input('Qual foi a distância em metros percorrida pelo patinete? '))
tempo = float(input('Quantos mminutos o patinete demorou para percorrer essa distância? '))
vel_media = distancia / tempo
print(f'O patinete atingiu uma velocidade de {vel_media:.2f} m/min')