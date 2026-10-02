from datetime import date


class Venda:
    def __init__(self, codigo: int, nome: str, valor: float, data: date) -> None:
        self._codigo = codigo
        self.nome = nome  # usa o setter
        self._valor = valor
        self._data = data

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome.strip().upper()

    @property
    def valor(self) -> float:
        return self._valor

    def classificar(self) -> str:
        if self._valor >= 100:
            return "Venda Alta"
        else:
            return "Venda Baixa"

    def __str__(self) -> str:
        return (
            f"Código: {self._codigo}\n"
            f"Cliente: {self._nome}\n"
            f"Valor: R${self._valor:.2f}\n"
            f"Data: {self._data.strftime('%d/%m/%Y')}"
        )


# Criando uma venda
v1 = Venda(1, "Fulano", 100.0, date(2024, 6, 1))

print(v1)

# Alterando o nome usando o setter
v1.nome = "Maria"

print("\nApós alteração:")
print(v1)