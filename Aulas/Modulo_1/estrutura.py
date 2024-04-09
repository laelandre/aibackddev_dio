# Indentação e blocos
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")


sacar(100)

# Estrutura condicionais
MAIOR_IDADE = 18

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("ainda não pode tirar a CNH")

# Estrutura de Repetição
texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

for numero in range (0, 51,5):
    print(numero, end=" ")