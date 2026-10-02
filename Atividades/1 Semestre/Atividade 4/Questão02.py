alunos = []
medias = []

while True:
    nome = str(input("Digite o nome do aluno (Ou 'sair'): "))
    if nome.lower() == "sair":
        break

    while True:
        media = float(input(f"Digite a média de {nome} (De 0 a 10): "))
        if 0 <= media <= 10:
            break
        else:
            print("Média inválida! Valor tem que ser de 0 a 10.")

    alunos.append(nome)
    medias.append(media)

print()
print("Lista de Alunos: ", alunos)
print()

print("-" * 40)
for i in range(len(alunos)):
    if medias[i] >= 6:
        situacao = "Aprovado"
    elif medias[i] <2:
        situacao = "Reprovado"
    else:
        situacao = "Recuperação"
        
    print(f"Nome: {alunos[i]} - {situacao}")
print("-" * 40)