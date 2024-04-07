nome = "AnDrE"

print(nome.upper)
print(nome.lower)
print(nome.title)

texto = "  Ola mundo!!   "

print(texto)
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu= "Python"

print(menu.center(14,"#"))
print("-".join(menu))



# Interpolação de Variaveis

nome2 = "André"
idade = 31

print("Nome: %s Idade: %s" % (nome2, idade))
print("Nome:{} Idade:{}".format(nome2, idade))
print("Nome:{name} idade:{age}".format(age=idade, name=nome2))

# Fatiamento de String

nome3 = "Andre Lael Rocha"

print(nome3[0])
print(nome3[-2])
print(nome3[:9])


# String mutiplas linhas
