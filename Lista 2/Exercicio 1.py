#  Crie um algoritmo que seja capaz de descobrir, por meio de perguntas lógicas (verdadeiro ou falso) 
# sobre características físicas, um animal que o usuário tenha em mente. Considere os animais: pato, 
# águia, galinha, avestruz, pinguim, morcego, ornitorrinco, leão, gato, onça pintada, baleia, tubarão, 
# lambari, enguia e arraia. 

print("Pense em um animal e responda as seguintes perguntas com Verdadeiro ou Falso.")

# Perguntas para identificar o animal
respostas = {
    "ave": input("O animal que você pensou é uma ave? "),
    "mamifero": input("O animal que você pensou é um mamífero? "),
    "peixe": input("O animal que você pensou é um peixe? "),
    "voa": input("O animal que você pensou voa? "),
    "nada": input("O animal que você pensou nada? "),
    "carnivoro": input("O animal que você pensou é carnívoro? "),
}

# Identifica o animal com base nas respostas
if respostas["ave"] == "Verdadeiro":
    if respostas["voa"] == "Verdadeiro":
        if respostas["carnivoro"] == "Verdadeiro":
            print("O animal que você pensou é uma águia.")
        else:
            print("O animal que você pensou é um pato.")
    else:
        if respostas["nada"] == "Verdadeiro":
            print("O animal que você pensou é um pinguim.")
        else:
            print("O animal que você pensou é uma avestruz.")
elif respostas["mamifero"] == "Verdadeiro":
    if respostas["voa"] == "Verdadeiro":
        print("O animal que você pensou é um morcego.")
    elif respostas["nada"] == "Verdadeiro":
        print("O animal que você pensou é uma baleia.")
    elif respostas["carnivoro"] == "Verdadeiro":
        print("O animal que você pensou é uma onça pintada.")
    else:
        print("O animal que você pensou é um leão.")
elif respostas["peixe"] == "Verdadeiro":
    if respostas["carnivoro"] == "Verdadeiro":
        print("O animal que você pensou é um tubarão.")
    else:
        print("O animal que você pensou é um lambari.")
else:
    print("O animal que você pensou é um ornitorrinco.")
