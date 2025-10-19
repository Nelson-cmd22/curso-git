aluno = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Média de {aluno}: {media:.1f}')

if media <= 5.0:
    print('Situação: Reprovado')
elif media <= 7.0:
    print('Situação: Recuperação')
else:
    print('Situação: Aprovado')
