try:
# Faça um programa que peça o primeiro nome do usuário.
    primeiro_nome = input('Qual o seu primeiro nome? ')
    nome_int = len(primeiro_nome)
# Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, 
# escreva"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
    if nome_int <= 4:
        print('Seu nome é curto!')
    elif nome_int >= 5 and nome_int <= 6:
        print('Seu nome é normal!')
    elif nome_int > 6:
        
        print('Seu nome é muito grande!')


except:
    print('Comando inválido!')