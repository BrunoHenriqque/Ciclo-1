#Crie um algoritmo que, dado três números informados pelo usuário, informe qual é o maior deles.

# Coloque os números
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

# Defina o maior entre os 3 
maior = max(num1, num2, num3)

# Exibe o resultado
print("O maior número informado é: ", maior)
