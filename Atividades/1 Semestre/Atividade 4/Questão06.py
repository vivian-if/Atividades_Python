lista1 = []
lista2 = []

tamanho = int(input("Digite o tamanho da lista: "))
print()

for i in range(tamanho):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista1.append(numero)

listaordem = sorted(lista1)
maior = max(lista1)
menor = min(lista1)

for x in lista1:
    lista2.append((x * maior) / menor)

print()
print("*" * 20)
print(lista1)
print("*" * 20)

print()
print("ORDEM CRESCENTE:")
print(listaordem)
print()
print("Maior número: ", maior)
print("Menor número: ", menor)
print()
print("Elementos da lista depois de multiplicar e dividir:")
print(lista2)