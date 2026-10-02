numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("Maior número:", round(numero1))
    print("Menor número:", round(numero2))

elif numero2 > numero1:
    print("Maior número:", round(numero2))
    print("Menor número:", round(numero1))

else:
    print("Os números são os mesmos.")
