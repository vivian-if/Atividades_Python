preco = float(input("Digite o preço do produto: R$ "))

if preco <= 50:
    novo_preco = preco + (preco * 0.05)
elif preco <= 100:
    novo_preco = preco + (preco * 0.10)
else:
    novo_preco = preco + (preco * 0.15)

if novo_preco <= 80:
    classificacao = "Barato"
elif novo_preco <= 120:
    classificacao = "Normal"
elif novo_preco <= 200:
    classificacao = "Caro"
else:
    classificacao = "Muito caro"

print(f"Novo preço: R$ {novo_preco:.2f}")
print("Classificação:", classificacao)
