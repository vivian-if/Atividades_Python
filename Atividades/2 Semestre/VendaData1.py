from datetime import date
VENDA_BARATA = "Barata"
VENDA_MEDIA = "Média"
VENDA_ALTA = "Alta"
class Venda:
    def __init__(self, codigo: int, nome: str, valor: float, data: date) -> None:
        self._codigo = codigo
        self._nome = nome
        self._valor = valor
        self._data = data

    @property
    def valor(self) -> float:
        return self._valor

    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome.strip().upper()

    def __str__(self) -> str:
        return (
            f"Código: {self._codigo}\nCliente: {self._nome}\n"
            f"Valor: R${self._valor:.2f}\nData: {self._data.strftime('%d/%m/%Y')}"
        )
    
    def classificar(self) -> str:
        if self._valor <100:
            tipo= VENDA_BARATA
        elif self._valor <500:
            tipo= VENDA_MEDIA
        else:
            tipo = VENDA_ALTA
        return tipo

v1 = Venda(1, "Fulano", 100.0, date(2024, 6, 1))

print(v1)
print(v1.valor)
v1.nome("Maria")
print(v1)