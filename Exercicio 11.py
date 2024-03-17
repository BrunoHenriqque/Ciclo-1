# Agora altere o algoritmo anterior de maneira que ele permita que o professor, antes de informar as notas, 
# informe os seus respectivos pesos. Depois disso o algoritmo deve, de análoga ao exercício anterior, 
# calcular a média, no entanto, agora considerando os seus pesos. Lembrete: A soma dos pesos das 
# notas sempre deve ser 10.

# Solicita ao usuário as quatro notas e seus respectivos pesos
nota1 = float(input("Informe a primeira nota: "))
peso1 = float(input("Informe o peso da primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
peso2 = float(input("Informe o peso da segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
peso3 = float(input("Informe o peso da terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
peso4 = float(input("Informe o peso da quarta nota: "))

# Verifica se a soma dos pesos é igual a 10
if peso1 + peso2 + peso3 + peso4 != 10:
    print("Erro: A soma dos pesos das notas deve ser 10.")
else:
    # Calcula a média 
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)

    # Verifica se o aluno foi aprovado ou reprovado
    if media >= 7.0:
        print("O aluno foi aprovado com média: ", media)
    else:
        print("O aluno foi reprovado com média: ", media)
