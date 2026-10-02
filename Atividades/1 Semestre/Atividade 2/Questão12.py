codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

if 1 <= codigo <= 10:
    preco_unitario = 10.00
elif 11 <= codigo <= 20:
    preco_unitario = 15.00
elif 21 <= codigo <= 30:
    preco_unitario = 20.00
elif 31 <= codigo <= 40:
    preco_unitario = 30.00
else:
    print("Código inválido!")

preco_total = preco_unitario * quantidade

if preco_total <= 250:
    desconto_percentual = 5
elif preco_total <= 500:
    desconto_percentual = 10
else:
    desconto_percentual = 15

valor_desconto = preco_total * (desconto_percentual / 100)
preco_final = preco_total - valor_desconto

print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
