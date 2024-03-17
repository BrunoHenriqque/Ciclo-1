# Crie um algoritmo que, dado três números informados pelo usuário, verifique se algum deles é múltiplo 
# de outro. Note que pode haver mais de um múltiplo entre eles. 

# Solicita ao usuário três números
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

# Verifica se algum número é múltiplo de outro
if num1 % num2 == 0 or num1 % num3 == 0:
    print("O primeiro número é múltiplo de pelo menos um dos outros.")
elif num2 % num1 == 0 or num2 % num3 == 0:
    print("O segundo número é múltiplo de pelo menos um dos outros.")
elif num3 % num1 == 0 or num3 % num2 == 0:
    print("O terceiro número é múltiplo de pelo menos um dos outros.")
else:
    print("Nenhum dos números é múltiplo de outro.")
