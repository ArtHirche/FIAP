rm = input('Insira seu RM: ')
idade = int(input('Digite sua idade: '))
email = input('Digite seu e-mail de contato: ')
if idade >= 18:
    print(f'Sua participação foi autorizada, aluno de RM: {rm}!')
    print(f'Mais informações serão enviadas ao e-mail: {email}.')
else:
    autorizacao = str(input('Você possui autorização dos responsáveis? [S/N] ')).upper()
    if autorizacao == 'S':
        print(f'Sua participação foi autorizada, aluno de RM: {rm}!')
        print(f'Mais informações serão enviadas ao e-mail: {email}.')
    else:
        print('Sua participação foi negada! Você deve ter 18 anos ou mais ou ter autorização de um responsável.')