limite = int(input("Quantos números da sequência de Fibonacci devem aparecer? "))
primeiro = 0
segundo = 1

print("Sequência de Fibonacci:")
print(primeiro)
print(segundo)

for i in range(2, limite):
    seguinte = primeiro + segundo
    print(seguinte)
    primeiro = segundo
    segundo = seguinte