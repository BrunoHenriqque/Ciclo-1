# Você viajou para os Estados Unidos e descobriu que lá a unidade de medida de temperatura é diferente 
# da do Brasil. Para não ter que acessar um serviço na internet a todo o momento, nem fazer os cálculos 
# manualmente, faça um algoritmo que converte a temperatura, dada uma unidade de medida e uma 
# temperatura. Ou seja, se a data for informada em Celsius o algoritmo deve fornecer a temperatura em 
# Fahrenheit, já se a temperatura for fornecida em Fahrenheit, o resultado deve ser em graus Celsius. 


# Solicita ao usuário a temperatura e a unidade de medida
temperatura = float(input("Informe a temperatura: "))
unidade = input("Informe a unidade de medida (C para Celsius, F para Fahrenheit): ")

# Converte a temperatura para a outra unidade de medida
if unidade.upper() == "C":
    temperatura_convertida = temperatura * 9/5 + 32
    print(f"A temperatura em Fahrenheit é {temperatura_convertida:.2f}°F")
elif unidade.upper() == "F":
    temperatura_convertida = (temperatura - 32) * 5/9
    print(f"A temperatura em Celsius é {temperatura_convertida:.2f}°C")
else:
    print("Unidade de medida desconhecida. Por favor, informe C para Celsius ou F para Fahrenheit.")
