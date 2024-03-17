# Faça um algoritmo que, dados três números inteiros, os imprima em ordem crescente

# Solicita ao usuário três números inteiros
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Ordena a lista em ordem crescente
numeros.sort()

# Imprime os números em ordem crescente
print("Os números em ordem crescente são: ", numeros)
