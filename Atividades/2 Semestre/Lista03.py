#CONSTANTES (C2):
CONSUMO_POR_PAGINA = 0.25
TONER_ALERTA = 15
TONER_MAXIMO = 100

#Criando a classe impressora (C1).
class Impressora:
    quantas_criadas = 0 #Variável para ir contando quantas vão ser feitas (C9).

    def __init__(self, nome, ip, modelo,
      #Opcionais:
        toner=TONER_MAXIMO, #Usa a constante TONER_MAXIMO (C2) com padrão 100.
        paginas_impressas=0): #Tem como padrão 0.

        self.nome = str(nome).strip().lower() #Nome sem espaço ou maiúsculo (C1).
        self.ip = ip  #Vai para o Setter (C4).
        self.modelo = str(modelo).strip() #Nome sem espaço (C1).
        self.toner = toner   #Vai para o Setter (C4).
        self.paginas_impressas = int(paginas_impressas) #Aceita apenas número.
        Impressora.quantas_criadas += 1 #Contar impressoras criadas (C9).

#Criar "@staticmethod ip_valido(texto)" que aceite números de 0-255 (C3).
    @staticmethod
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

#Transformando Ip em property (C3).
    @property
    def ip(self):
        return self._ip

#Recusando valores inválidos de IP (C3).
    @ip.setter
    def ip(self, valor):
        if Impressora.ip_valido(valor):
            self._ip = valor
        else:
            print("IP inválido, tente novamente.")
            self._ip = "Ip inválido"

#Transformar toner em property (C4).
    @property
    def toner(self):
        return self._toner

#Toner vai aceitar números inteiros ou decimais entre 0 e TONER_MAXIMO (C4).
    @toner.setter
    def toner(self, valor):
        if isinstance(valor, (int, float)) and 0 <= valor <= TONER_MAXIMO:
            self._toner = valor
        else:
            print("Por favor, coloque somente valores entre 0 e ", TONER_MAXIMO, ".")
            self._toner = 0 
            
#Botando o modelo/interface que vai aparecer (C5).
    def __str__(self):
        aviso = "[OK]" if self.toner >= TONER_ALERTA else "[!!]"
        toner_texto = str(round(self.toner, 1))
        return (
            aviso + " " + 
            self.nome.ljust(20) + " " + 
            str(self.ip).ljust(15) + " toner " + 
            toner_texto.rjust(5) + "% " + 
            str(self.paginas_impressas).rjust(4) + " pag."
        )

#Método que recusa quantidade de páginas que não seja inteiro positivos e recusar o trabalho se o toner não for suficiente (C6).
    def imprimir(self, paginas):
        if not isinstance(paginas, int) or paginas <= 0:
            print("O número de páginas precisa ser inteiro positivo.")
            return False
        
        if paginas > self.paginas_restantes:
            print(f"Toner insuficiente para {paginas} páginas (dá para {self.paginas_restantes}).") #Valor varia de acordo com o "x.imprimir(numero)"
            return False
        
        self.toner -= paginas * CONSUMO_POR_PAGINA
        self.paginas_impressas += paginas
        return True
    
#Método de trocar_toner que retorna ele ao máximo. (C7)
    def trocar_toner(self):
        self.toner = TONER_MAXIMO
        
#Acrescentando duas properties calculadas (C8).
    @property
    def precisa_trocar(self):
        return self.toner <= TONER_ALERTA #Volta como True se atingir a condição
        
    @property
    def paginas_restantes(self):
        return int(self.toner // CONSUMO_POR_PAGINA) #Calcular quantas páginas ainda podem ser impressas
    
#Adicionando classmethod (C9).
    @classmethod
    def quantas(classe):
        return classe.quantas_criadas

    @classmethod
    def de_texto(classe, linha):
        partes = [espaço.strip() for espaço in linha.split(";")]
        nome, ip, modelo, toner = partes
        return classe(nome, ip, modelo, float(toner))


#Classmethod acima permite imprimir tudo em uma linha (C9) como o exemplo abaixo.
print("[EXEMPLO DA C9]".center(50))
exemplo = "hp-lab1 ; 10.0.0.50 ; HP M404 ; 87"
exemplo_da_C9 = Impressora.de_texto(exemplo)
print(exemplo_da_C9)

print()
impressoes = [
    Impressora("Impressora A", "10.0.0.50", "Modelo1", 32),
    Impressora("Impressora B", "10.125.40.50", "Modelo2", 42.0, 180),
    Impressora("Impressora C", "200.140.40.51", "Modelo3", 14.5, 30),
]

print("[EXEMPLO ALEATÓRIO]".center(50))
print()
for imprimir in impressoes:
    print(imprimir)

print()
print("[EXEMPLO DA C8]".center(50))
print()
print("Toner atual:", imprimir.toner)
print("Paginas restantes:", imprimir.paginas_restantes)
imprimir.imprimir(70)