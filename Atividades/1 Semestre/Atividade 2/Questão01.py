nota1 = float(input("Digite quanto tirou no seminário:"))
nota2 = float(input("Digite quanto tirou de atividades:"))
nota3 = float(input("Digite sua nota da prova:"))
nota4 = float(input("Digite sua nota pela presença:"))
media = nota1 + nota2 + nota3 + nota4 / 4
print("Sua média ficou:", media)
if media >= 7:
    print("Meus parabéns, você passou!")
else:
    print("Você está de recuperação!")
