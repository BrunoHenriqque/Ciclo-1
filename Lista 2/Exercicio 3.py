# Agora altere esse algoritmo para que imprima os números em ordem decrescente.

# Solicita ao usuário três números
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Mostre o resultado da sequencia
print("Os números em ordem decrescente são: ", numeros)
