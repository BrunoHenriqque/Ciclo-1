# Agora altere o algoritmo anterior de maneira que ele verifique os demais níveis de alerta. Considere: 0-
# 3 é "BAIXO", maior que 3 até 6 "MÉDIO", maior que 6 até 9 "ALTO", para os demais casos é considerado 
# "GRAVE"

# Solicita ao usuário o nível de alerta de risco
nivel_alerta = float(input("Informe o nível de alerta de risco (0 a 10): "))

# Verifica se o nível de alerta está entre 0 e 10
if 0 <= nivel_alerta <= 10:
    # Verifica o nível de alerta
    if nivel_alerta <= 3:
        print("O nível de alerta é BAIXO.")
    elif nivel_alerta <= 6:
        print("O nível de alerta é MÉDIO.")
    elif nivel_alerta <= 9:
        print("O nível de alerta é ALTO.")
    else:
        print("O nível de alerta é GRAVE.")
else:
    print("Erro: O nível de alerta informado deve estar entre 0 e 10.")
