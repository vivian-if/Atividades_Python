produtos = []
precos = []

while True:
    nome = str(input("Digite o nome do produto (Ou 'sair'): "))
    if nome.lower() == "sair":
        break
    preco = float(input("Digite seu preço: "))
    print()

    produtos.append(nome)
    precos.append(preco)

caro = precos.index(max(precos))
barato = precos.index(min(precos))

print()
print(f"Produto mais caro: {produtos[caro]} - R$ {precos[caro]}")
print(f"Produto mais barato: {produtos[barato]} - R$ {precos[barato]}")
print()

reajuste = []
print("REAJUSTES DE PREÇOS:")
for preco in precos:
    if preco <= 20:
        reajuste.append(preco * 1.10)
    else:
        reajuste.append(preco * 1.05)

for i in range(len(produtos)):
    print(f"{produtos[i]} - R$ {reajuste[i]:.2f}")

caro_reajuste = reajuste.index(max(reajuste))
barato_reajuste = reajuste.index(min(reajuste))

print()
print(f"Produto mais caro: {produtos[caro_reajuste]} - R$ {reajuste[caro_reajuste]:.2f}")
print(f"Produto mais barato: {produtos[barato_reajuste]} - R$ {reajuste[barato_reajuste]:.2f}")