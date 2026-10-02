funcionarios = []

while True:
    print("\n===== FOLHA DE PAGAMENTOS =====")
    print("1 - Adicionar funcionário")
    print("2 - Buscar funcionário")
    print("3 - Gerar relatório")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome: ")

        while True:
            matricula = int(input("Matrícula: "))

            existe = False
            for funcionario in funcionarios:
                if funcionario["matricula"] == matricula:
                    existe = True
                    break

            if existe:
                print("Matrícula já cadastrada.")
            else:
                break

        setor = input("Setor: ")

        while True:
            carga = int(input("Carga horária (20 ou 40): "))
            if carga == 20 or carga == 40:
                break
            print("Carga horária inválida.")

        while True:
            salario = float(input("Salário base: "))
            if 2000 <= salario <= 10000:
                break
            print("Salário inválido.")

        funcionario = {
            "nome": nome,
            "matricula": matricula,
            "setor": setor,
            "carga": carga,
            "salario": salario
        }

        funcionarios.append(funcionario)

        print("Funcionário cadastrado com sucesso!")

    elif opcao == "2":

        matricula = int(input("Digite a matrícula: "))

        encontrado = False

        for funcionario in funcionarios:
            if funcionario["matricula"] == matricula:

                print("\nNome:", funcionario["nome"])
                print("Matrícula:", funcionario["matricula"])
                print("Setor:", funcionario["setor"])
                print("Carga horária:", funcionario["carga"])
                print("Salário base: R$", funcionario["salario"])

                encontrado = True
                break

        if not encontrado:
            print("Matrícula não encontrada.")

    elif opcao == "3":

        if len(funcionarios) == 0:
            print("Nenhum funcionário cadastrado.")
        else:

            soma = 0

            print("\n===== RELATÓRIO =====")

            for funcionario in funcionarios:

                if funcionario["carga"] == 40:
                    salario_final = funcionario["salario"] * 1.20
                else:
                    salario_final = funcionario["salario"] * 1.10

                soma += salario_final

                print("-----------------------------")
                print("Nome:", funcionario["nome"])
                print("Matrícula:", funcionario["matricula"])
                print("Setor:", funcionario["setor"])
                print("Carga-horária:", funcionario["carga"], "horas")
                print("Salário base: R$", funcionario["salario"])
                print("Salário final: R$", salario_final)

            media = soma / len(funcionarios)

            print("-----------------------------")
            print("Total dos salários finais: R$", soma)
            print("Salário final médio: R$", media)

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")