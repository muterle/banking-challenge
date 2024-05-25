menu = """
Menu
1 = Depositar
2 = Realizar Saque
3 = Exibir Extrato
0 = Sair
"""

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input('Informe a opção:')

    if opcao == '1':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Depósito realizado com sucesso! Seu saldo é de R$ {saldo:.2f}')
        else:
            print('Erro! Valor do depósito deve ser maior que zero.')
    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))
        if valor > 0 and valor <= saldo and numero_saque < LIMITE_SAQUES:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1
            print(f'Saque realizado com sucesso! Seu saldo é de R$ {saldo:.2f}')
        elif valor > saldo:
            print('Você não tem saldo suficiente para realizar este saque.')
        elif numero_saque >= LIMITE_SAQUES:
            print('Você atingiu o limite de saques diários.')
        else:
            print('Erro! Valor do saque deve ser maior que zero.')
    elif opcao == '3':
        print('Extrato:')
        print('Sem movimentações' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
    elif opcao == '0':
        print('Fechando aplicação...')
        break
    else:
        print('Opção inválida. Tente novamente.')