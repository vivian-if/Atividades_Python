#CONSTANTES (C2):
CONSUMO_POR_PAGINA = 0.25
TONER_ALERTA = 15
TONER_MAXIMO = 100

def ip_valido(texto):
    quatro_partes = texto.split(".") #Dividindo os IP em 4 números e pontos.
    if len(quatro_partes) != 4: #Se não forem quatro, não funciona.
        return False
    for parte in quatro_partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255: #Só entre 0 e 255.
            return False
    return True