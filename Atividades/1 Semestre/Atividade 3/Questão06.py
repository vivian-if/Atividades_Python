total_vista = 0
total_parcela = 0
menor = None
maior = None

for i in range(1, 16):
    codigo = input(f"Digite o código da {i}ª compra (V para vista / P para parcela): ").upper()
    valor = float(input("Digite o valor da compra: "))

    if valor <= 0:
        print("ERRO! O valor da compra deve ser maior que 0.")
        continue

    print("R$", valor)

    if codigo == "V":
        total_vista += valor
    elif codigo == "P":
        total_parcela += valor
    else:
        print("ERRO! Use apenas V ou P.")
        continue

    if menor is None or valor < menor:
        menor = valor
    if maior is None or valor > maior:
        maior = valor

total_geral = total_vista + total_parcela

print("TRANSAÇÕES RESULTADOS:")
print(f"Total das compras à vista: R$ {total_vista:.2f}")
print(f"Total das compras a prazo: R$ {total_parcela:.2f}")
print(f"Menor compra: R$ {menor:.2f}")
print(f"Maior compra: R$ {maior:.2f}")
print()
print(f"Total geral das compras: R$ {total_geral:.2f}")
