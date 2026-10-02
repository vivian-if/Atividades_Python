Valor = int(input("Digite o valor do saque: "))

Nota100 = Valor // 100
Valor = Valor % 100
Nota50 = Valor // 50
Valor = Valor % 50
Nota20 = Valor // 20
Valor = Valor % 20
Nota10 = Valor // 10
Valor = Valor % 10
Nota5 = Valor // 5
Valor = Valor % 5
print()
print("Resultado:")
print()
print("Notas de 100:", Nota100)
print("Notas de 50:", Nota50)
print("Notas de 20:", Nota20)
print("Notas de 10:", Nota10)
print("Notas de 5:", Nota5)
