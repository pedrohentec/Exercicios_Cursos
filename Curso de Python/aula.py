nome = 'Marnelly' # 7 caracteres
#       01234567
tamanho_nome = len(nome) # 8 int
resultado = ' '
indice = 0

while indice < tamanho_nome:
    resultado += '*' + nome[indice]
    indice += 1

print(resultado)