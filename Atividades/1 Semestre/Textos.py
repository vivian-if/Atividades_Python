texto = input(str("Digite seu texto: "))
primeira = 1

semespaco = texto.replace(" ", "").lower()
palavras = texto.count (" ")
inverter = texto[::-1].lower()
palindromo = inverter.replace(" ", "")

print()
print("Quantidade de palavras:")
print(palavras + primeira)
print()
print("Quantidade de caracteres (Contando espaço):")
print(len(texto))
print()
print("Quantidade de caracteres (Sem espaço):")
print(len(semespaco))
print()
print("Texto invertido:")
print(inverter.capitalize())
print("O texto é palíndromo?")
if semespaco == palindromo:
    print("Sim")
else:
    print("Não")