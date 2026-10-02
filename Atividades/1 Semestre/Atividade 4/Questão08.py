tamanho = int(input("Digite o tamanho que deseja para lista: "))

lista = []
print()
for numero in range(tamanho):
    preencher = int(input(f"Digite o {numero + 1 }º número da lista: "))
    lista.append(preencher)

print()
print("-" * 50)
print(f"Sua lista {lista}")
print("-" * 50)

contados = []
print()
for n in lista:
    if n not in contados:
        total = lista.count(n)
        print(f"O número {n} aparece {total} vezes na lista.")
        contados.append(n)