inicial = int(input("Digite o numero inicial:"))
final = int(input("Digite o numero final:"))
contador = 1

print("TABUADA")

for i in range(inicial, final + 1):
    soma = inicial + i
    multiplicaçao = inicial * i
    print(f"{inicial} + {i} = {soma} | {inicial} x {i} = {multiplicaçao}")
