alario = float(input("Digite o seu salário: "))

if salario < 500:
    aumento = salario * 0.30
    novo_salario = salario + aumento

    print("Salário reajustado: R$", novo_salario)

else:
    print("Desculpe, você não tem direito ao aumento.")
