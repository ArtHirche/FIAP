pagar = 0
faturamento_anual = float(input('Qual o seu faturamento anual? R$ '))
assinatura = int(input('Qual o seu nível de assinatura?\n(1) Basic - 30%;\n(2) Silver - 20%;\n(3) Gold - 10%;\n(4) Platinum - 5%;\nOPÇÃO: '))
if assinatura == 1:
    pagar = faturamento_anual * 0.3
    print(f'O bônus será de 30%, totalizando R$ {pagar:.2f}')
elif assinatura == 2:
    pagar = faturamento_anual * 0.2
    print(f'O bônus será de 20%, totalizando R$ {pagar:.2f}')
elif assinatura == 3:
    pagar = faturamento_anual * 0.10
    print(f'O bônus será de 10%, totalizando R$ {pagar:.2f}')
elif assinatura == 4:
    pagar = faturamento_anual * 0.05
    print(f'O bônus será de 5%, totalizando {pagar:.2f}')
