min = int(input('Digite os minutos atuais: '))
fat = 1
for n in range(1, min + 1):
    fat *= n
senha = 'LIBERDADE'
print(f'Senha necessária: {senha}{fat}')