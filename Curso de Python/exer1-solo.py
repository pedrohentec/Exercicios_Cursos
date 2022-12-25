# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. 
while True:
    try:
        numero = input('Digite um número inteiro: ')
        numero_int = int(numero)
        if numero_int % 2 == 0:
            print(f'o número {numero_int} é par.')
        else:
            print(f'o número {numero_int} é ímpar.')
# Caso o usuário não digite um número inteiro, informe que não é um número inteiro
    except:
        print('Você não digitou um número inteiro.')
    continuar = input('Você deseja recomeçar ? [S/N] ').upper()
    if continuar == 'S':
        continue
    else:
        break