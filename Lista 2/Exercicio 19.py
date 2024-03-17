# Faça um algoritmo que, dado o valor total em reais e o número de prestações desejadas, calcule o valor 
# de cada prestação. O número mínimo de prestações deve ser 12. Se o número de prestações for maior 
#ou igual a 24, adicione 10% de juros ao valor total, se for maior ou igual a 36, adicione 15% de juros ao 
# valor total

# Solicita ao usuário o valor total e o número de prestações
valor_total = float(input("Informe o valor total em reais: "))
prestacoes = int(input("Informe o número de prestações desejadas (mínimo 12): "))

# Verifica se o número de prestações é válido
if prestacoes < 12:
    print("O número mínimo de prestações é 12.")
else:
    # Adiciona os juros ao valor total, se necessário
    if prestacoes >= 36:
        valor_total *= 1.15  # Adiciona 15% de juros
    elif prestacoes >= 24:
        valor_total *= 1.10  # Adiciona 10% de juros

    # Calcula o valor de cada prestação
    valor_prestacao = valor_total / prestacoes

    # Imprime o valor de cada prestação
    print(f"O valor de cada prestação é: R$ {valor_prestacao:.2f}")
