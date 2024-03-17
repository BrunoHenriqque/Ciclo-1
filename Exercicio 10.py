# Considerando o sistema de notas da UniEVANGÉLICA, construa um algoritmo que, dadas 4 notas 
# parciais de um aluno pelo usuário, calcule a média e imprima se o aluno foi aprovado ou reprovado. 
# Considere os 3 ciclos.

# Solicita ao usuário as quatro notas
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verifica se o aluno foi aprovado ou reprovado
if media >= 70.0:
    print("O aluno foi aprovado com média: ", media)
else:
    print("O aluno foi reprovado com média: ", media)
