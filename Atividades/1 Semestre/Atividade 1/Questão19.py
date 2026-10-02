Hora = int(input("Digite sua hora: "))
Minutos = int(input("Digite seus minutos: "))

HoraMinutos = Hora * 60
TotalMinutos = HoraMinutos + Minutos
Segundos = TotalMinutos * 60

print("Hora em minutos:", HoraMinutos)
print("Total em minutos:", TotalMinutos)
print("Total em segundos:", Segundos)