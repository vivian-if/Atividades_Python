Salario = float(input("Qual o salário de João? "))
Conta1 = float(input("Digite quanto foi a primeira conta: "))
Conta2 = float(input("Digite quanto foi a segunda conta: "))
Descontado1 = Conta1 + (Conta1 * 0.02)
Descontado2 = Conta2 + (Conta2 * 0.02)
Gastou = Descontado1 + Descontado2
Sobrou = Salario - Gastou
print("João acabou ficando com", round(Sobrou))