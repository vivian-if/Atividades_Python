"""
LISTA 2 | Estudo dirigido: Relacionamentos entre objetos.

Nome: Vivian do Nascimento Gomes

Este e o arquivo onde voce trabalha. Siga o roteiro do documento da
Lista 4, etapa por etapa. Ao terminar cada etapa:

    1. abra o arquivo conferir.py e mude a linha ETAPA;
    2. rode conferir.py
    3. so siga em frente quando todos os testes derem OK.

CENARIO
    Uma companhia aerea. Passageiros fazem reservas; cada reserva pode
    ter um assento; cada voo nasce com os seus assentos e recebe uma
    tripulacao que tambem trabalha em outros voos.
"""


# ======================================================================
# Passageiro
# ======================================================================
class Passageiro:
    def __init__(self, nome: str, documento: str) -> None:

# ETAPA 1: guarde nome (sem espacos sobrando) e documento
        self.nome = str(nome).strip()
        self.documento = str(documento)
# ETAPA 2: comece com uma lista vazia de reservas
        self.reservas = []

# ETAPA 1: devolva algo como "Ana Souza (111)"
    def identificacao(self) -> str:
        return f"{self.nome} ({self.documento})"

# ETAPA 5: escreva __eq__ (passageiros iguais = mesmo documento)
    def __eq__(self, outro):
        return self.documento == outro.documento
    
# ======================================================================
# Assento
# ======================================================================
class Assento:
    def __init__(self, codigo: str) -> None:
        # ETAPA 2: guarde o codigo; o assento comeca sem passageiro
        self.codigo = codigo
        self.passageiro = None

    def esta_livre(self) -> bool:
# ETAPA 2
        return self.passageiro is None

    def ocupar(self, passageiro: Passageiro) -> bool:
# ETAPA 2: recuse (avise e devolva False) se ja estiver ocupado;
#          caso contrario, guarde o passageiro e devolva True
        if not self.esta_livre():
                    print(f"assento {self.codigo} ja esta ocupado")
                    return False
        
        self.passageiro = passageiro
        return True


    def liberar(self) -> None:
# ETAPA 2
        self.passageiro = None


# ======================================================================
# Reserva
# ======================================================================
class Reserva:
    def __init__(self, codigo: str, passageiro: Passageiro) -> None:
# ETAPA 1: guarde o codigo e o OBJETO passageiro
        self.codigo = codigo
        self.passageiro = passageiro
# ETAPA 2: comece sem assento, e avise o passageiro desta reserva
        self.assento = None
        passageiro.reservas.append(self)

# ETAPA 2: acrescente o assento: "R1 | Ana Souza (111) | 1A"
#          ou "R1 | Ana Souza (111) | sem assento"
    def cartao(self) -> str:
        if self.assento is None:
            return f"{self.codigo} | {self.passageiro.identificacao()} | sem assento"
        return f"{self.codigo} | {self.passageiro.identificacao()} | {self.assento.codigo}"

# ETAPA 2: escreva marcar_assento(assento)
    def marcar_assento(self, assento) -> bool:
        if assento.ocupar(self.passageiro):
            self.assento = assento
            return True

        return False

# ======================================================================
# Tripulante
# ======================================================================
class Tripulante:
    def __init__(self, nome: str, funcao: str) -> None:
# ETAPA 3
        self.nome = nome
        self.funcao = funcao


# ======================================================================
# Voo
# ======================================================================
class Voo:
    def __init__(self, numero: str, origem: str, destino: str,
                 fileiras=5, letras="ABCD") -> None:
# ETAPA 3: guarde os dados e comece com a tripulacao vazia
# ETAPA 4: acrescente os parametros fileiras=5 e letras="ABCD"
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.tripulacao = []
#          e crie aqui dentro todos os assentos do voo
        self.letras = letras
        self.assentos = []

# ETAPA 5: comece tambem com uma lista vazia de reservas
        for fileira in range(1, fileiras + 1):
             for letra in letras:
                self.assentos.append(
                    Assento(f"{fileira}{letra}")
                )

        self.reservas = []

 # ETAPA 3: inclua o tripulante, sem repetir
# ETAPA 5: troque para escalar(self, *tripulantes)
    def escalar(self, *tripulantes) -> None:
# ETAPA 3
        for tripulante in tripulantes:
            if tripulante in self.tripulacao:
                print(f"{tripulante.nome} ja esta no voo {self.numero}")
            else:
                self.tripulacao.append(tripulante)

    def dispensar(self, tripulante: Tripulante) -> None:
# ETAPA 3
        if tripulante in self.tripulacao:
            self.tripulacao.remove(tripulante)

# ETAPA 4: escreva buscar_assento(codigo)
    def buscar_assento(self, codigo):
        for assento in self.assentos:
            if assento.codigo == codigo:
                return assento

        return None

# e assentos_livres()
    def assentos_livres(self):
        livres = 0

        for assento in self.assentos:
            if assento.esta_livre():
                livres += 1

        return livres

# ETAPA 5: escreva primeiro_livre(), reservar(...) e __len__

    def primeiro_livre(self):
        for assento in self.assentos:
            if assento.esta_livre():
                return assento

        return None

    def reservar(self, passageiro, codigo_assento=None):

        for reserva in self.reservas:
            if reserva.passageiro == passageiro:
                print(f"{passageiro.nome} ja tem reserva no voo {self.numero}")
                return None
        if codigo_assento is None:
            assento = self.primeiro_livre()
        else:
            assento = self.buscar_assento(codigo_assento)
        if assento is None or not assento.esta_livre():
            print(f"assento indisponivel no voo {self.numero}")
            return None

        codigo_reserva = f"{self.numero}-{len(self.reservas) + 1}"
        reserva = Reserva(codigo_reserva, passageiro)
        reserva.marcar_assento(assento)
        self.reservas.append(reserva)
        return reserva

    def __len__(self):
        ocupados = 0
        for assento in self.assentos:
            if not assento.esta_livre():
                ocupados += 1

        return ocupados

# ETAPA 6: escreva mapa() e resumo()
    def mapa(self):
        linhas = []
        fileiras = int(self.assentos[-1].codigo[:-1])
        
        for numero in range(1, fileiras + 1):
            assentos_fileira = []
            for letra in self.letras:
                assento = self.buscar_assento(f"{numero}{letra}")
                if assento.esta_livre():
                    status = "."
                else:
                    status = "X"
                assentos_fileira.append(f"{assento.codigo:>3} {status}")
            linhas.append("  ".join(assentos_fileira))

        return "\n".join(linhas)

    def resumo(self):
        return (
            f"Voo {self.numero} {self.origem}->{self.destino}: "
            f"{len(self)} ocupados, "
            f"{self.assentos_livres()} livres, "
            f"{len(self.tripulacao)} tripulantes"
        )

# ======================================================================
# ETAPA 6: o programa final
# ======================================================================
if __name__ == "__main__":
    voo = Voo("AZ101", "NAT", "REC", fileiras=3)
    voo.escalar(
        Tripulante("Eduarda", "piloto"),
        Tripulante("Erika", "comissario")
    )

    passageiro1 = Passageiro("Eloise", "111")
    passageiro2 = Passageiro("Vivian", "222")
    passageiro3 = Passageiro("Isabele", "333")

    reserva1 = voo.reservar(passageiro1, "2C")
    reserva2 = voo.reservar(passageiro2)

    voo.reservar(passageiro3, "2C")
    reserva3 = voo.reservar(passageiro3, "3D")

    voo.reservar(
        Passageiro("Iasmin", "111")
    )

    print()
    print(voo.resumo())
    print()
    print(voo.mapa())
    print()

    for reserva in voo.reservas:
        print(reserva.cartao())