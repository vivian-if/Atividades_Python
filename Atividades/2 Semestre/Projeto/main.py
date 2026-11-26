from impressoras import Impressora, __init__, validacao

#Criando as 4 impressoras (C10).
imprime = [
    "Impressora a ; 10.0.0.50 ; Modelo1 ; 80",
    "Impressora b ; 192.168.23.40 ; Modelo2 ; 100",
    "Impressora c ; 200.140.40.51 ; Modelo3 ; 70",
    "Impressora d ; 10.125.40.50 ; Modelo4 ; 65"
]

impressoras = [Impressora.de_texto(linha) for linha in imprime]

#Simulando uma uma sequência de trabalhos de impressão, mostrando os recusados (C10).
print("[SIMULAÇÃO DE IMPRESSÕES]".center(50))
print()
for impressao in impressoras:
    for paginas in [30, 70, 200]:  # alguns testes
        resultado = impressao.imprimir(paginas)
        if not resultado:
            print(f"ERRO: {impressao.nome} não conseguiu imprimir {paginas} páginas.")

print()
#Listando todas as impressoras (C10).
print("LISTAGEM DE IMPRESSORAS".center(50))
print()
for impressao in impressoras:
    print(impressao)

print()
#Mostrar as que precisam trocar o toner (C10).
print("PRECISAM TROCAR TONER".center(50))
print()
for impressao in impressoras:
    if impressao.precisa_trocar:
        print(impressao)

#Mostrar total de páginas impressas (C10).
total_paginas = sum(impressao.paginas_impressas for impressao in impressoras)
print("Total de páginas impressas:", total_paginas)
print()

#Mostrando alguns exemplos de valores inválidos
print("TESTES DE VALORES INVÁLIDOS".center(50))

print()
#IP Errado:
impressao_invalida = Impressora("impressora casa", "400.230.257.0", "modelo 1.0", 50)
print(impressao_invalida)

#Toner inválido (0 a 100%):
impressao_invalida = Impressora("impressora staff", "10.0.0.10", "modelo 2.0", 200)
print(impressao_invalida)

#Quantidade de páginas não aceitáveis:
impressao_invalida = Impressora("impressora reserva", "10.0.0.11", "modelo 3.0", 50)
impressao_invalida.imprimir(-5)
impressao_invalida.imprimir(3.5)
