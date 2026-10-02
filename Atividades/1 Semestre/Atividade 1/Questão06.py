Peso = float(input("Digite o peso que você tinha semana passada: "))
Aumentou = (Peso * 15) / 100
Engordou = Peso + Aumentou
Reduziu = (Peso * 20) / 100
Emagreceu = Peso - Reduziu
print("Você engordou 15%, agora seu peso é:", round(Engordou,2),"kg")
print("Você emagreceu 20%, agora seu peso é:", round(Emagreceu,2),"kg")
