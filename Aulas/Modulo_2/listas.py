# Conteudo sobre listas

frutas = ["maçã", "laranja", "banana", "uva"]

# Filtros V1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)

# Filtros V2
numeros2 = [1, 30, 21, 2, 9, 65, 34]
pares2 = [numeros2 for numero2 in numeros2 if numero2 % 2 == 0]