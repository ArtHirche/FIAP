pontuacao = int(input('Insira a pontuação do cliente: '))
telefone_contato = int(input('Insira um número de contato: +55 '))
if pontuacao >= 1000:
    print('O cliente tem direito a receber mais 3GB na sua franquia de internet!')
    print(f'Entraremos em contato com o número +55 {telefone_contato} para confirmar o requerimento do bônus')
elif pontuacao >= 500:
    print('O cliente tem direito a receber mais 1,5GB na sua franquia de internet!')
    print(f'Entraremos em contato com o número +55 {telefone_contato} para confirmar o requerimento do bônus')
elif pontuacao >= 200:
    print('O cliente tem direito a receber mais 500MB na sua franquia de internet!')
    print(f'Entraremos em contato com o número +55 {telefone_contato} para confirmar o requerimento do bônus')
else:
    print('O cliente não tem direito a receber bônus, sintimos muito!')
