seg = int(input('Digite a quantidade de votos para segunda-feira: '))
ter = int(input('Digite a quantidade de votos para terça-feira: '))
qua = int(input('Digite a quantidade de votos para quarta-feira: '))
qui = int(input('Digite a quantidade de votos para quinta-feira: '))
sex = int(input('Digite a quantidade de votos para sexta-feira: '))
escolhido = ''
mais_votado = -1
if seg > mais_votado:
    mais_votado = seg
    escolhido = 'segunda-feira'
if ter > mais_votado:
    mais_votado = ter
    escolhido = 'terça-feira'
if qua > mais_votado:
    mais_votado = qua
    escolhido = 'quarta-feira'
if qui > mais_votado:
    mais_votado = qui
    escolhido = 'quinta-feira'
if sex > mais_votado:
    mais_votado = sex
    escolhido = 'sexta-feira'
print(f'O dia escolhido para as lives é {escolhido} com {mais_votado} votos.')
