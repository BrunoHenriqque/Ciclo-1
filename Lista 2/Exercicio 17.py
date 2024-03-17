#  Problemas simples do cotidiano podem representar desafios para o mundo computacional. Faça um 
# algoritmo que, dados três números inteiros representando dia, mês e ano de uma data, imprima qual o 
# dia seguinte. 

from datetime import datetime, timedelta

# Solicita ao usuário a data
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))

# Cria um objeto datetime com a data informada
data = datetime(ano, mes, dia)

# Calcula o dia seguinte
dia_seguinte = data + timedelta(days=1)

# Imprime o dia seguinte
print("O dia seguinte é: ", dia_seguinte.day, "/", dia_seguinte.month, "/", dia_seguinte.year)
