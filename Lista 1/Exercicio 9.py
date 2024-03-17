# Crie um algoritmo que, dados os lados de um triângulo informados pelo usuário, calcule a área.

import math

# Solicita ao usuário o tamanho de três lados
lado1 = float(input("Informe o tamanho do primeiro lado: "))
lado2 = float(input("Informe o tamanho do segundo lado: "))
lado3 = float(input("Informe o tamanho do terceiro lado: "))

# Calcula a semi-perímetro
s = (lado1 + lado2 + lado3) / 2

# Calcula a área usando a fórmula
area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))

# Exibe o resultado
print("A área do triângulo é: ", area)
