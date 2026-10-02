tamanho = int(input("Digite o tamanho que deseja para lista: "))

lista = []
print()
for numero in range(tamanho):
    preencher = float(input(f"Digite o {numero + 1 }º número da lista: "))
    lista.append(preencher)

soma = sum(lista)

produto = 1
for i in lista:
    produto *= i

print()
print("LISTA")
print(lista)
print()

print()
extra1 = ""
extra2 = ""

for i in range(len(lista)):
    extra1 = extra1 + str(lista[i])

    if i < len(lista) - 1:
        extra1 = extra1 + " + "

extra1 = extra1 + " = " + str(soma)

print(extra1)
print("-" * 30)

for i in range(len(lista)):
    extra2 = extra2 + str(lista[i])

    if i < len(lista) - 1:
        extra2 = extra2 + " * "

extra2 = extra2 + " = " + str(produto)

print(extra2)