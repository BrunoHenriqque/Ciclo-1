# Crie um algoritmo que, dado o nível de alerta de risco, imprima se ele for GRAVE. O nível de alerta é
# um número que varia de 0 a 10. O nível é considerado GRAVE quando ele é superior a 9

# Solicita ao usuário o nível de alerta de risco
nivel_alerta = float(input("Informe o nível de alerta de risco (0 a 10): "))

# Verifica se o nível de alerta é GRAVE
if nivel_alerta > 9:
    print("O nível de alerta é GRAVE.")
else:
    print("O nível de alerta não é GRAVE.")
