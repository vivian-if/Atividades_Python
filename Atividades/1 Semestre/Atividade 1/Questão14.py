import math

a = float(input("Digite o valor do cateto A: "))
b = float(input("Digite o valor do cateto B: "))
h = math.sqrt(a**2 + b**2)
print("A hipotenusa é:", round(h))
