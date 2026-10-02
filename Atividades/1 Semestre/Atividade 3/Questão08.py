altura = int(input("Digite a altura: "))
largura = int(input("Digite a largura: "))

for linha in range(altura):
    if linha == 0 or linha == altura - 1:
        print("* " * largura)  #CIMA / BAIXO
    else:
        print("* " + "  " * (largura - 2) + "*")  #MEIO