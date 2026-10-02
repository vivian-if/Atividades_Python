while True:
    numero = int(input("Digite um número inteiro que queira a fatorial: "))
    if numero < 0:
        print("Por favor, tente novamente")
        continue
    else:
        break

fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {numero} é {fatorial}")