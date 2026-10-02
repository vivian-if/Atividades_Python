numeros = []
tamanho = int(input("Digite o tamanho da lista: "))
print()

for i in range(tamanho):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

print()
print(numeros)
print()

dividir2 = [n for n in numeros if n % 2 == 0]
dividir3 = [n for n in numeros if n % 3 == 0]
dividir2e3 = [n for n in numeros if n % 2 == 0 and n % 3 == 0]

print("Numeros dívisiveis por 2: ", dividir2)
print("Numeros dívisiveis por 3: ", dividir3)
print("Numeros dívisiveis por 2 e 3: ", dividir2e3)