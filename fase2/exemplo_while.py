resposta = '0'
while resposta != '42':
    resposta = input('Qual a resposta para a vida, o universo e tudo mais?')
    if resposta != '42':
        print('Não. Você errou!')
print('Parabéns, você acertou!')