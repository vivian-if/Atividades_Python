pessoas = 0
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for pessoas in range (1, 16):
    dados = int(input("Digite sua idade:" ))

    if dados <= 15:
        faixa1 += 1
    elif dados <= 30:
        faixa2 += 1
    elif dados <= 45:
        faixa3 += 1
    elif dados <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

print()

print(f"1ª faixa (-15): {faixa1} pessoas")
print(f"2ª faixa (16-30 anos): {faixa2} pessoas")
print(f"3ª faixa (31-45 anos): {faixa3} pessoas")
print(f"4ª faixa (46-60 anos): {faixa4} pessoas")
print(f"5ª faixa (+60 anos): {faixa5} pessoas")
