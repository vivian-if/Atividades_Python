salario = float(input("Digite o seu salário: "))

if salario <= 300:
    aumento = salario * 0.35

else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print("Salário reajustado: R$", novo_salario)
