numero = int(input("Digite um número:"))
print()
print()
print("MULTIPLICAÇÃO:")
for i in range(1,51):
    print(f"{numero} x {i} = {numero * i}")
print()
print("ADIÇÃO:")
soma = 0
for i in range(1,50):
    soma += numero
    print(f"{numero} + {i} = {numero + soma}")
