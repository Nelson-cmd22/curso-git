def mostrar_menu():
    print('\n=== Caixa Eletrônico ===')
    print('1 - Consultar Saldo')
    print('2 - Sacar dinheiro')
    print('3 - Sair')

def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            print(f'{quantidade} cédula(s) de R$ {cedula}')
            valor -= quantidade * cedula

saldo = 1000

while True:
    mostrar_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(f'Seu saldo atual é: R$ {saldo:.2f}')

    elif opcao == '2':
        saque = float(input('Digite o valor de saque: '))

        if saque < 1 or saque > 1000:
            print('Valor inválido, (Permitido entre 10 e 1000)')
        elif saque > saldo:
            print('Saldo insuficiente')
        else:
            print('Você receberá:')
            calcular_cedulas(saque)
            saldo -= saque
            print(f'Seu novo saldo é: R$ {saldo: .2f}')

    elif opcao == '3':
        print('Obrigado por usar o caixa eletrônico. Até logo!')
        break

    else:
        print('Opção inválida, tente novamente.')
