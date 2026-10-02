quantidade = int(input("Digite a quantidade de números da lista: "))
numeros = []
print()

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

print()

print("Números inseriods: ", numeros)

numeros.reverse()
print("Números na ordem inversa:", numeros)

print()

print("_______________ ")
print("Forma 1 de mostrar os pares!!")

for n in numeros:
    if n % 2 == 0:
        print(f"Número par: {n}")

print("_______________ ")
print("Forma 2 de mostrar os pares!!")

pares1 = []
for n in numeros:
    if n % 2 == 0:
        pares1.append(n)

print("Números pares: ", pares1)

print("_______________ ")
print("Forma 3 de mostrar os pares!!")

pares2 = [n for n in numeros if n % 2 == 0]
print("Números pares: ", pares2)
print("Quantidade de números pares: ", len(pares2))

menor = numeros[0]
for n in numeros:
    if n < menor:
        menor = n

maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n

print()

print("Menor valor da lista: ", min(numeros))
print("Menor valor da lista (Usando loop): ", menor)
print("Menor valor da lista: ", max(numeros))
print("Menor valor da lista (Usando loop): ", maior)

print()

contados = []

for n in numeros:
    if n not in contados:
        total = numeros.count(n)
        print(f"O número {n} aparece {total} vezes na lista")
        contados.append(n)