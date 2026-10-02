numeros_lidos = 0
maior_numero = 0
somatorio = 0

while True:
    numero = int(input("Digite um número inteiro (0 pra encerrar):"))

    if numero == 0:
        break
    elif numero < 0:
        continue

    numeros_lidos += 1
    somatorio += numero

    if numero > maior_numero:
        maior_numero = numero

media_aritmetica = somatorio / numeros_lidos

print(f"Números lidos: {numeros_lidos}")
print(f"Maior número: {maior_numero}")
print(f"Média aritmética: {int(media_aritmetica)}")
