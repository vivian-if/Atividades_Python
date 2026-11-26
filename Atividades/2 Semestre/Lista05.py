from abc import ABC, abstractmethod
def reais(centavos: int) -> str:
    return f"R$ {centavos // 100},{centavos % 100:02d}"

#Q7: Criando classe cobravel para herdar ABC (Abstract Base Class).
class Cobravel(ABC):
    @abstractmethod
    def valor(self) -> int: #Vai precisar de valor.
        pass #Não faz nada ainda.

    @abstractmethod
    def descricao(self) -> str: #Vai precisar de descrição.
        pass #Não faz nada ainda.

#Q1: Criando classe Veiculo para herdar ABC (Abstract Base Class).
#Q7: Trocando para a classe herdar a classe cobravel que já tem o ABC, logo todo "objeto" cobravel deverá informar.
class Veiculo(Cobravel):
    def __init__(self, #Construtor geral dos objetos/veiculos.
    placa: str, #Não possui padrão, é obrigatório informar.
    horas: int = 0 #Padrão é 0 horas.
    ) -> None:
        self.placa = placa.strip().upper() #Str em maiúscula e sem espaço.
        self.horas = horas #Int.

    def descricao(self) -> str: #Q7: Metódo para aceitar descrição.
        return f"{self.tipo()} {self.placa} ({self.horas}h)"

    @abstractmethod #Metódo para definir quanto custa uma hora de estacionamento.
    def tarifa_hora(self) -> int:
        pass #Não faz nada ainda.

    @abstractmethod #Metódo para o veículo informar o tipo.
    def tipo(self) -> str:
        pass #Não faz nada ainda.

    def valor(self) -> int: #Metódo que cálcula o valor total.
        return self.tarifa_hora() * self.horas

    def __str__(self) -> str: #Formato de exibição.
        return f"{self.descricao()} {reais(self.valor())}"

#Q2: Criando os tipos carro, moto e caminhão herdando de Veiculo (Recebendo placa, horas, valor e o formato).
class Carro(Veiculo): #Classe carro herdando veículo.
    def tarifa_hora(self) -> int: #Metódo que informa o valor/tarifa.
        return 1000  #Vai custar 10,00 conto por hora (1000 centavos).

    def tipo(self) -> str: #Metódo que informa o tipo carro.
        return "Carro"


class Moto(Veiculo): #Classe moto herdando veículo.
    def tarifa_hora(self) -> int: #Metódo que informa o valor/tarifa.
        return 500  #Vai custar 5,00 conto por hora (500 centavos).

    def tipo(self) -> str: #Metódo que informa o tipo moto.
        return "Moto"

#Parte da Q3:
    def valor(self) -> int: #Metódo que dá o valor final depois do desconto.
        return max(0, super().valor() - self.tarifa_hora()) #Chama o metódo valor de Veiculo e desconta a primeira hora (-500), garantindo que nunca fique negativo com "max".


class Caminhao(Veiculo): #Classe caminhão herdando veículo, mas precisa criar um novo construtor.
    def __init__(self, #Construtor próprio pra receber os eixos.
    placa: str, #Não possui padrão, é obrigatório informar.
    eixos: int = 1,  #Padrão é 1 eixo.
    horas: int = 0 #Padrão é 0 horas.
    ) -> None:
        super().__init__(placa, horas) #trás os self do construtor veículo.
        self.eixos = eixos #int com a adição dos eixos.

    def tarifa_hora(self) -> int: #Metódo que informa o valor/tarifa.
        return 800 * self.eixos #Vai custar 8,00 conto (800 centavos) por cada eixo.

    def tipo(self) -> str: #Metódo que informa o tipo caminhão.
        return "Caminhao"

    def descricao(self) -> str: #Formato de exibição específico pros eixos do caminhão.
        return f"{self.tipo()} {self.eixos} eixos {self.placa} ({self.horas}h)"

#Q3: Criando o tipo carro elétrico herdando de carro, pagando metade da tarifa (Primeira hora grátis).
class CarroEletrico(Carro): #Classe carro elétrico herdando carro.
    def tarifa_hora(self) -> int: #Metódo que informa o valor/tarifa.
        return super().tarifa_hora() // 2 #Chama o metódo de tarifa/hora da classe Carro (10 conto por hora) e faz divisão inteira (//) por 2.

    def tipo(self) -> str: #Metódo que informa o tipo carro elétrico.
        return "Carro eletrico"

#Q4: Criando uma função independente para relatório.
def relatorio(veiculos: list[Veiculo]) -> int: #Irá receber uma lista de veículos.
    total = 0 #Começará com 0 e vai aumentando.

    for veiculo in veiculos: #Vai ver os veículos armazenados.
        print(veiculo) #Mostrá-los.
        total += veiculo.valor() #E então somá-los.

    print(f"Total: {reais(total)}")
    return total #Trás os resultados da conta.

#Q5: Criando filtro de valores e o tipo van.
#Criando uma função independente para definir o mais caro.
def mais_caro(veiculos: list[Veiculo]) -> Veiculo: #Irá receber uma lista de veículos.
    maior = veiculos[0] #Pega o primeiro veículo para comparar.

    for veiculo in veiculos: #Vai ver os veículos armazenados.
        if veiculo.valor() > maior.valor(): #Momento da comparação.
            maior = veiculo

    return maior #Trás o resultado do veículo com maior valor.

#Criando uma função independente para o filtro.
def filtrar_por_valor( #Construtor próprio para:
    veiculos: list[Veiculo], #Receber uma lista de veículos.
    minimo: int #Definir o mínimo.
) -> list[Veiculo]: #Manda tudo pra lista.
    resultado: list[Veiculo] = [] #Vai mostrar o resultado na lista filtrada.

    for veiculo in veiculos: #Vai ver os veículos armazenados.
        if veiculo.valor() >= minimo: #Comparar e ver se está acima do mínimo.
            resultado.append(veiculo) #Adicona a lista se atingir a condição.

    return resultado #Trás o resultado da lista renovada.

class Van(Veiculo): #Classe van herdando veiculo.
    def tarifa_hora(self) -> int: #Metódo que informa valor/tarifa.
        return 1200 #Vai custar 12,00 conto por hora (1200 centavos).

    def tipo(self) -> str: #Metódo que informa o tipo van.
        return "Van"

#Q6: Somar os eixos e usar isinstance.
#Criando uma função independente para o total de eixos.
def total_eixos(veiculos: list[Veiculo]) -> int:
    total = 0 #O total começa com 0 eixos e vai aumentando.

    for veiculo in veiculos: #Vai ver os veículos armazenados.
        if isinstance(veiculo, Caminhao): #Retorna True ou False para pergunta se o objeto é um caminhão.
            total += veiculo.eixos #Se for, soma no total.

    return total #Trás o resultado do total de eixos.

#Q7: Criando mais uma classee e metódo.
class Lavagem(Cobravel): #Classe lavagem herdando cobravel.
    def __init__(self, #Construtor próprio para:
    placa: str, #Receber a placa do veículo obrigatória.
    completa: bool #Saber se é completa ou não.
    ) -> None:
        self.placa = placa.strip().upper() #Str em maiúscula e sem espaço.
        self.completa = completa #Só recebe true ou false.

    def valor(self) -> int: #Metódo que calcula quanto custa a lavagem.
        if self.completa: #Se for completa:
            return 6000 #Será 60,00 conto (6000 centavos).
        return 2500 #Se não, será 25,00 conto (2500 centavos).

    def descricao(self) -> str: #Metódo para receber a descrição sobre a lavagem.
        if self.completa: #Se ela for completa:
            return f"Lavagem completa {self.placa}" #Fala que é completa e informa a placa do veículo.
        return f"Lavagem simples {self.placa}" #Fala que é incompleta e informa a placa do veículo.

    def __str__(self) -> str:
        return f"{self.descricao()} {reais(self.valor())}"

def fechar_caixa(itens: list[Cobravel]) -> int: #Irá receber uma lista de cobráveis.
    total = 0 #Começa com 0 e vai aumentando.

    for item in itens: #Vai ver os itens (veículos ou lagagens) armazenados.
        print(item) #Mostra eles.
        total += item.valor() #Soma no caixa.

    print(f"caixa do dia: {reais(total)}") #Converte centavo pra real.

    return total #Mostra os resultados.

#Q8: Criar uma classe para o estacionamento chamado patio.
class Patio: #Classe patio que vai possuir uma capacidade e lista de veículos.
    def __init__(self, #Construtor próprio para:
    capacidade: int #Int de número de vagas
    ) -> None:
        self.capacidade = capacidade #Definir o máximo de veículos.
        self.veiculos: list[Veiculo] = [] #Criar uma lista para armazenar os veículos do patio.
    
    def entrar(self, veiculo: Veiculo) -> bool: #Informa com true ou false se entrou um veículo.
        for v in self.veiculos: #Procura na lista dos veículos.
            if v.placa == veiculo.placa: #Uma placa idêntica.
                print(f"placa ja presente: {veiculo.placa}") #Informa que já está estacionada.
                return False #Então recusa.

        if len(self.veiculos) >= self.capacidade: #Conta os veículos na lista para ver se é maior que a capacidade.
            print(f"patio lotado: {veiculo.placa} nao entrou") #Tem veículos demais, então:
            return False #Recusa.

        self.veiculos.append(veiculo) #Adiciona um veículo na lista.
        return True

    def sair(self, #Construtor próprio para:
    placa: str, #Receber placa
    horas: int #Receber número de horas.
    ) -> int:
        placa = placa.strip().upper() #Placa vai ser minúscula sem espaço.

        for veiculo in self.veiculos: #Procura na lista dos veículos.
            if veiculo.placa == placa: #Se achar o veículo da placa:
                veiculo.horas = horas #Vai registrar as horas.

                valor = veiculo.valor() #Calcular valor.
                self.veiculos.remove(veiculo) #Tira o "objeto"/veículo do patio.
                return valor #Diz o valor a pagar.

        print(f"placa {placa} nao encontrada") #Informa que não encontrou a placa.
        return 0 #Trás 0.

    def ocupacao(self) -> str: #Mostra quantas vagas tão ocupadas.
        return f"{len(self.veiculos)}/{self.capacidade} vagas ocupadas" #x/x vagas.

#Saída Q1
print("Primeira questão:".center(75))
print("Traceback (most recent call last):")
print('  File "pratica_estacionamento.py", line 28, in <module>')
print('    Veiculo("ABC1234")')
print("TypeError: Can't instantiate abstract class Veiculo without an implementation")
print("for abstract methods 'tarifa_hora', 'tipo'")

print()

#Teste Q2
print("Segunda questão:".center(75))
gol = Carro("abc1d23", 3)
scania = Caminhao("cam7f89", 3, 2) #3 eixos e 2 horas.
print(gol)
print(scania)

print()

#Teste Q3
print("Terceira questão:".center(75))
biz = Moto("mot4e56", 2)
leaf = CarroEletrico("ele1t11", 3)
rapida = Moto("rap2d22", 1)
print(biz)
print(leaf)
print(rapida)

print()

#Teste Q4
print("Quarta questão:".center(75))
dia: list[Veiculo] = [gol, biz, scania, leaf, rapida]
relatorio(dia)

print()

#Teste Q5
print("Quinta questão:".center(75))
dia.append(Van("van3c33", 4))
print("mais caro:", mais_caro(dia))
for v in filtrar_por_valor(dia, 3000):
    print(v)

print()

#Teste Q6
print("Sexta questão:".center(75))
print(total_eixos(dia))

print()

#Teste Q7
print("Sétima questão:".center(75))
itens: list[Cobravel] = [gol, Lavagem("abc1d23", completa=True),
biz, Lavagem("mot4e56", completa=False)]
fechar_caixa(itens)

print()

#Teste Q8
print("Oitava questão:".center(75))
patio = Patio(2)
patio.entrar(Carro("aaa1a11"))
patio.entrar(Moto("bbb2b22"))
patio.entrar(Van("ccc3c33"))
print(patio.ocupacao())
print("saida AAA1A11:", reais(patio.sair("aaa1a11", 2)))
print(patio.ocupacao())