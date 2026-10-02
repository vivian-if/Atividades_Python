total = 0

while True:
    codigo = int(input("Digite o código do produto (0 para encerrar): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade comprada: "))

    print()

    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código Inválido!")
        continue

    total += preco * quantidade
    print(f"Produto de R$ {preco} comprado {quantidade} vezes")
    print(f"Total dos produtos: R$ {preco * quantidade:.2f}")

    print()

print ()

print("Calculando tudo...")
print(f"Seu total de compras foi: R$ {total:.2f}")
