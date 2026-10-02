import math

Raio = float(input("Digite o raio: "))

Comprimento = 2 * math.pi * Raio
Area = math.pi * Raio ** 2
Volume = (4 * math.pi * Raio ** 3) / 3

print("Comprimento:", round(Comprimento))
print("Área:", round(Area))
print("Volume:", round(Volume))
