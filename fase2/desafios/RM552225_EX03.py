soma_imp = 0
soma_par = 0
cont_imp = 0
cont_par = 0
for c in range(1, 51, 2):
    print('Você está digitando as notas dos alunos \033[1mIMPARES\033[m.')
    nota = float(input(f'Por favor, insira a nota do aluno de número {c}: '))
    soma_imp += nota
    cont_imp += 1
for p in range(2, 51, 2):
    print('Você está digitando as notas dos alunos \033[1mPARES\033[m.')
    nota = float(input(f'Por favor, insira a nota do aluno de número {p}: '))
    soma_par += nota
    cont_par += 1
media_imp = soma_imp / cont_imp
media_par = soma_par / cont_par
if media_imp > media_par:
    print(f'A metade dos alunos ímpares somou a maior nota. A média dos pares foi {media_par:.2f} e a dos ímpares foi {media_imp:.2f}.')
elif media_par > media_imp:
    print(f'A metade dos alunos pares obteve a maior nota. A média dos pares foi {media_par:.2f} e a dos ímpares foi {media_imp:.2f}.')
else:
    print(f'Ambas as metades tiveram a mesma média. A média dos pares foi {media_par:.2f} e a dos ímpares foi {media_imp:.2f}.')
