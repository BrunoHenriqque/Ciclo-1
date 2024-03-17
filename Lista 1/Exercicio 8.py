# Crie um algoritmo que, dados o tamanho de três lados informados pelo usuário, verifique se: (1) é um 
# triângulo isósceles, (2) é equilátero, (3) é escaleno ou (4) não é um triângulo.

# Solicita o tamanho de três lados
lado1 = float(input("Informe o tamanho do primeiro lado: "))
lado2 = float(input("Informe o tamanho do segundo lado: "))
lado3 = float(input("Informe o tamanho do terceiro lado: "))

# Verifica se os lados formam um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os lados informados não formam um triângulo.")
