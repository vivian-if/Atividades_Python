inteiros = []

while True:
    numero = int(input("Digite um número inteiro (Ou digite '0' para parar): "))
    if numero > 0:
        inteiros.append(int(numero))
    elif numero == 0:
        break
    else:
        print("Por favor, botar somente NÚMERO inteiro maior que 0.")
        continue

print()
print("Conjunto: ", inteiros)
print()

reverter = inteiros.reverse()

print("Inverso:", inteiros)

normaldenovo = inteiros.reverse()

print()
par = []
impar = []
pares = 0
impares= 0


for numero in inteiros:
    if numero % 2 == 0:
        par.append(numero)
        pares += 1
    else:
        impar.append(numero)
        impares+=1

print("Números pares: ", par)
print("Números impares: ", impar)
print()
print("Quantidade de números pares: ",pares)
print("Quantidade de números ímpares: ", impares)

if len(inteiros) > 0:
    menor = inteiros[0]
    maior = inteiros[0]
    for numero in inteiros:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero

print()
print("Menor número: ", menor)
print("Maior número: ", maior)

javistos = []

print()
for numero in inteiros:
    if numero not in javistos:
        contador = 0
        for isto in inteiros:
            if isto == numero:
                contador += 1
        print(f"{numero} aparece {contador} vezes")
        javistos.append(numero)