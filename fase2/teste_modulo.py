import teste.calc

valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')
opcao = int(input('Qual operação deseja fazer?\n1- Soma;\n2- Subtração;\n3- Divisão;\n4- Multiplicação;\n5- Encerrar.'))
while opcao != 5:
    if opcao == 1:
        somar = teste.calc.soma(valor1, valor2)
        print(f'A soma é: {somar}')
    elif opcao == 2:
        subtrair = teste.calc.subtracao(valor1, valor2)
        print(f'A subtração é: {subtrair}')
    elif opcao == 3:
        dividir = teste.calc.divisao(valor1, valor2)
        print(f'A divisão é {dividir}')
    elif opcao == 4:
        multiplicar = teste.calc.multiplicacao(valor1, valor2)
        print(f'A multiplicação é {multiplicar}')
    elif opcao == 5:
        break
