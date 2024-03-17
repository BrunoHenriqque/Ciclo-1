# Agora altere o algoritmo anterior de maneira que ele verifique também se o nível informado está entre 0 
# e 10. Caso contrário uma mensagem de erro deve ser apresenta.

# Solicita o nível de alerta de risco
nivel_alerta = float(input("Informe o nível de alerta de risco (0 a 10): "))

# Verifica se o nível de alerta está entre 0 e 10
if 0 <= nivel_alerta <= 10:
    if nivel_alerta > 9:
        print("O nível de alerta é GRAVE.")
    else:
        print("O nível de alerta não é GRAVE.")
else:
    print("Erro: O nível de alerta informado deve estar entre 0 e 10.")
