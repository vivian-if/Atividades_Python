saldo_medio = float(input("Qual seu saldo médio? "))

if saldo_medio > 400:
    credito = saldo_medio * 0.30
elif saldo_medio >= 300:
    credito = saldo_medio * 0.25
elif saldo_medio >= 200:
    credito = saldo_medio * 0.20
else:
    credito = saldo_medio * 0.10

print(f"Seu saldo médio: R$ {saldo_medio:.2f}")
print(f"Portanto o valor do crédito será: R$ {credito:.2f}")
