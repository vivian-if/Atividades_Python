num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("ESCOLHA UMA OPÇÃO:")
print("1 - Média entre os números")
print("2 - Diferença do maior pelo menor")
print("3 - Produto entre os números")
print("4 - Divisão do primeiro pelo segundo")
print("5 - Primeiro número elevado ao segundo")
print("6 - Raiz quadrada dos números")
print("7 - Raiz cúbica dos números")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    media = (num1 + num2) / 2
    print("Média:", media)

elif opcao == 2:
    if num1 > num2:
        diferenca = num1 - num2
    else:
        diferenca = num2 - num1

    print("Diferença:", diferenca)

elif opcao == 3:
    produto = num1 * num2
    print("Produto:", produto)

elif opcao == 4:
    divisao = num1 / num2
    print("Divisão:", divisao)

elif opcao == 5:
    potencia = num1 ** num2
    print("Resultado:", potencia)

elif opcao == 6:
    raiz1 = num1 ** 0.5
    raiz2 = num2 ** 0.5

    print("Raiz quadrada do primeiro número:", raiz1)
    print("Raiz quadrada do segundo número:", raiz2)

elif opcao == 7:
    raiz1 = num1 ** (1/3)
    raiz2 = num2 ** (1/3)

    print("Raiz cúbica do primeiro número:", raiz1)
    print("Raiz cúbica do segundo número:", raiz2)

else:
    print("Erro! Opção inválida.")