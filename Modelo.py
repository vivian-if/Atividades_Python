aviso = "Teste"
nome = "Maria"
ip = 33162
outro_numero = 15.2
numero = 42

print(f"{aviso} {nome:<10} {ip:<12} conteudo {outro_numero:5.1f}% {numero:4d}")

print(
    aviso + " " + 
    nome.ljust(10) + " " + 
    str(ip).ljust(12) + " conteudo " + 
    str(round(outro_numero, 1)).rjust(4) + "% " + 
    str(numero).rjust(4)
)