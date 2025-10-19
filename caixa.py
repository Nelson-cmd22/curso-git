cedulas = [100, 50, 20, 10, 5, 2, 1]

while True:
    valor = int(input('Digite o valor para saque (entre 10 e 600): '))
    if 10 <= valor <=600:
        break
    else:
        print('Valor inválido! Tente Novamente')

print('Você receberá: ')

for cedulas in cedulas:
    quantidade = valor // cedulas

    if quantidade > 0:
        print(f'{quantidade} cédula(s) de $ {cedulas}')
    valor = valor - (quantidade * cedulas)


