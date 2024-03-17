# Escreva um algoritmo para cadastro de dados básicos de alunos. O usuário deve informar o número da 
# matrícula (cinco dígitos), nome completo do aluno, gênero (o usuário deve informar “M” ou “F”), curso 
# (o usuário deve informar “BES”, “BEC” ou “ADS”) e coeficiente de rendimento (dever ser maior ou igual 
# a zero e menor ou igual a 100). Como resultado o sistema deve imprimir a matrícula, o nome do aluno, 
# gênero (deve imprimir “Masculino” ou “Feminino”), curso (“Bacharelado em Engenharia de Software” 
# para “BES”, “Bacharelado em Engenharia de Computação” para “BEC” e “Analise e Desenvolvimento 
# de Sistemas” para “ADS”), o coeficiente de rendimento, seguido por “Excelente” se o coeficiente for [90, 
# 100], “Bom” se entre [70, 90), “Regular” se entre [50, 70), “Necessita melhoras” se entre [30, 50) e 
# “Preocupante” se entre [0, 30). Note a existência de intervalos fechados e semifechados para os 
# coeficientes.

# Solicita ao usuário os dados do aluno
matricula = input("Informe o número da matrícula (cinco dígitos): ")
nome = input("Informe o nome completo do aluno: ")
genero = input("Informe o gênero do aluno (M ou F): ")
curso = input("Informe o curso do aluno (BES, BEC ou ADS): ")
coeficiente = float(input("Informe o coeficiente de rendimento do aluno (0 a 100): "))

# Converte o código do curso para o nome completo
if curso == "BES":
    curso = "Bacharelado em Engenharia de Software"
elif curso == "BEC":
    curso = "Bacharelado em Engenharia de Computação"
elif curso == "ADS":
    curso = "Analise e Desenvolvimento de Sistemas"

# Converte o gênero para o nome completo
if genero == "M":
    genero = "Masculino"
elif genero == "F":
    genero = "Feminino"

# Determina a avaliação do coeficiente de rendimento
if 90 <= coeficiente <= 100:
    avaliacao = "Excelente"
elif 70 <= coeficiente < 90:
    avaliacao = "Bom"
elif 50 <= coeficiente < 70:
    avaliacao = "Regular"
elif 30 <= coeficiente < 50:
    avaliacao = "Necessita melhoras"
elif 0 <= coeficiente < 30:
    avaliacao = "Preocupante"

# Imprime os dados do aluno
print("\nDados do aluno:")
print("Matrícula:", matricula)
print("Nome:", nome)
print("Gênero:", genero)
print("Curso:", curso)
print("Coeficiente de rendimento:", coeficiente, "-", avaliacao)
