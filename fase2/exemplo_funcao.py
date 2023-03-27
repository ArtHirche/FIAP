def calcularVelocidadeMedia(a, b):
    velocidade_media = a / b
    return velocidade_media
distancia = float(input('Digite a distância percorrida: '))
tempo = float(input('Digite o tempo da viagem: '))
print(f'A velocidade média é {calcularVelocidadeMedia(distancia, tempo)}')