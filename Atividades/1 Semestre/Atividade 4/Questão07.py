quantosalunos = int(input("Digite o número de alunos: "))

lista1 = []
lista2 = []

print()
for e in range(quantosalunos):
    nome = str(input(f"Digie o nome do(a) {e + 1}º aluno(a): "))
    lista1.append(nome)
    print()

    notasgeral = []
    for i in range(4):
        nota = float(input(f"Digite sua {i+1}º nota: "))
        notasgeral.append(nota)
    total = sum(notasgeral)
    media = total/4

    if media >= 7:
        situacao = "Aprovado"
    elif media < 3:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
        
    print()
    print("Nome: ", nome)
    print("Notas: ", notasgeral)
    print("Soma das notas: ",total)
    print("Média Aritmética: ", media)
    print("Situação: ", situacao)
    print()

    lista1.append(notasgeral)
    lista2.append([nome, notasgeral, total, media, situacao])

print()

print("-" * 50)
for aluno in lista2:
    print(f"Aluno: {aluno[0]}".center(50))
    print(f"Média: {aluno[3]}".center(50))
    print(f"Situação: {aluno[4]}".center(50))
    print("-" * 50)

aprovados =[aluno[0] for aluno in lista2 if aluno[4] == "Aprovado"]
recuperacao =[aluno[0] for aluno in lista2 if aluno[4] == "Recuperação"]
reprovados =[aluno[0] for aluno in lista2 if aluno[4] == "Reprovado"]

print()
print()
print()
print("=== CONSIDERAÇÕES FINAIS ===".center(50))
print()
print()
print()

print("APROVADOS:")
if aprovados:
    for nome in aprovados:
        print(nome.center(20))
else:
    print("---------".center(20))

print("RECUPERAÇÃO:")
if recuperacao:
    for nome in recuperacao:
        print(nome.center(20))
else:
    print("---------".center(20))

print("REPROVADOS:")
if reprovados:
    for nome in reprovados:
        print(nome.center(20))
else:
    print("---------".center(20))