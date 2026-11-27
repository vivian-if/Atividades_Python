class Produto:
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco
    def descricao(self) -> str:
        return self.nome

coisa = Produto("Coisa", 1000)

from abc import ABC, abstractmethod
class Produto(ABC):
    def __init__(self, nome: str, preco: int) -> None:
        self.nome = nome
        self.preco = preco
    
    @abstractmethod
    def descricao(self) -> str:
        pass
        
class Prato(Produto):
    def __init__(self, nome: str, preco: int, serve: int) -> None:
        super().__init__(nome, preco)
        self.serve = serve
            
    def descricao(self) -> str:
        return f"{self.nome} (serve {self.serve})"

from collections import deque #Não é algo sequencial como uma lista, portanto é mais rápido
fila = deque(["p101", "p102"]) #Simula o conceito de filas
fila.append("p103") #Nenhum precisa andar pra frente com deque
fila.popleft()
