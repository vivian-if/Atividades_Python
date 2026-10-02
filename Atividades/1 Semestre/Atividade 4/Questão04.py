tamanho1 = int(input("Digite o tamanho da 1º lista: "))

lista1 = []
lista2 = []

print()
print("Peço que preencha a primeira lista.")
for e in range(tamanho1):
    nome = str(input(f"Digite o {e+1}º nome: "))
    lista1.append(nome)

print()
print("LISTA 1:")
print(lista1)

print()
tamanho2 = int(input("Digite o tamanho da 1º lista: "))

print()
print("Peço que preencha a segunda lista.")
for e in range(tamanho2):
    nome = str(input(f"Digite o {e+1}º nome: "))
    lista2.append(nome)

print()
print("LISTA 2:")
print(lista2)

print()
print("LISTA 3:")
lista3 = lista1 + lista2
lista3.sort()
print(lista3)