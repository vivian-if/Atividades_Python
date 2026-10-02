numero = int(input("Digite um número: "))

print("TABUADA DE ADIÇÃO")
print(numero, "+ 1 =", numero + 1)
print(numero, "+ 2 =", numero + 2)
print(numero, "+ 3 =", numero + 3)
print(numero, "+ 4 =", numero + 4)
print(numero, "+ 5 =", numero + 5)
print(numero, "+ 6 =", numero + 6)
print(numero, "+ 7 =", numero + 7)
print(numero, "+ 8 =", numero + 8)
print(numero, "+ 9 =", numero + 9)
print(numero, "+ 10 =", numero + 10)

print("TABUADA DE MULTIPLICAÇÃO")
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

print()
print()

print("\t Versão simplificada que aprendi na net>>>>")

print()
numero = int(input("Digite um número: "))
print("TABUADA DE ADIÇÃO")
for i in range(1, 11):
    print(numero, "+", i, "=", numero + i)
print("TABUADA DE MULTIPLICAÇÃO")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
