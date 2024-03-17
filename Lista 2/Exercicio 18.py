# Agora, crie um algoritmo que imprima o dia anterior da data informada

from datetime import datetime, timedelta

# Solicita ao usuário a data
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

# Cria um objeto datetime com a data informada
data = datetime(ano, mes, dia)

# Calcula o dia anterior
dia_anterior = data - timedelta(days=1)

# Imprime o dia anterior
print("O dia anterior é: ", dia_anterior.day, "/", dia_anterior.month, "/", dia_anterior.year)
