from .validacao import CONSUMO_POR_PAGINA, TONER_ALERTA, TONER_MAXIMO, ip_valido

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

#Transformando IP em property (C3)
    @property
    def ip(self):
        return self._ip

#Recusando valores inválidos de IP (C3).
    @ip.setter
    def ip(self, valor):
        if ip_valido(valor):
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
            print("Por favor, coloque valores entre 0 e ", TONER_MAXIMO, ".")
            self._toner = 0 

#Botando o modelo/interface que vai aparecer (C5).
    def __str__(self):
        aviso = "[OK]" if self.toner >= TONER_ALERTA else "[!!!]"
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