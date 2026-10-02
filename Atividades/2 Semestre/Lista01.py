#Questão B3 (criando constantes)
#OBRIGATÓRIAS:
ABERTO = "aberto"
ATENDIMENTO = "atendimento"
RESOLVIDO = "resolvido"
#OPCIONAIS (ficarão em padrão caso contrário):
ALTA = "alta"
MEDIA = "media"
BAIXA = "baixa"

#Questão B1 (classe com as partes obritagórias e as opcionais que se não preenchidas vão entrar no padrão)
#Questão B2 (string, lower e title)
class Chamado:

    def __init__(self, titulo, solicitante,
                 prioridade=MEDIA,
                 situacao=ABERTO,
                 tempo_atendimento=24):

        self.titulo = titulo.strip()
        self.solicitante = solicitante.strip().title()
        self.situacao = situacao.strip().lower()

        self._prioridade = MEDIA
        self.prioridade = prioridade

        self._tempo_atendimento = 24
        self.tempo_atendimento = tempo_atendimento

#Questão B6 parte 1 (transformar prioridade em property)
    @property
    def prioridade(self):
        return self._prioridade

#Questão B3 (colocando outros níveis de prioridade além de média)
    @prioridade.setter
    def prioridade(self, valor):
        valor = valor.strip().lower()

        prioridades_validas = [ALTA, MEDIA, BAIXA]

#Questão B6 parte 2 (escrever um setter)
        if valor in prioridades_validas:
            self._prioridade = valor
        else:
            print("Por favor, coloque um valor válido.")

#Questão B7 (setter recusar o que não for número inteiro)
    @property
    def tempo_atendimento(self):
        return self._tempo_atendimento

    @tempo_atendimento.setter
    def tempo_atendimento(self, valor):

        if not isinstance(valor, int):
            print("Número inválido.")
            return

        if valor < 0:
            print("Número inválido.")
            return

        self._tempo_atendimento = valor

#Questão B8 (adicionar property que devolva o tempo em minutos)
    @property
    def minutos_gastos(self):
        return self.tempo_atendimento * 60

#Questão B4 (devolver True para resolvido ou somar horas)
    def esta_resolvido(self):
        return self.situacao == RESOLVIDO
    def aumentar_tempo(self, horas):
        self.tempo_atendimento += horas

#Questão B5 (definindo formato)
    def __str__(self):
        return (f"[{self.prioridade.upper():5}] "
                f"{self.titulo:25} | "
                f"{self.solicitante:20} | "
                f"{self.tempo_atendimento:3}h")

#Questão B9 (tentando "estragar" o chamado)
print("QUESTÃO B9".center(50, "-"))
print("A prioridade 'urgentissima' não existe e o tempo")
print("de atendimento só pode ser número inteiro. Logo,")
print("as mensagens de erro programadas irão aparecer:")
print("-" * 50)
print()
c = Chamado("Computador travando", "ana paula", "alta")

c.prioridade = "urgentissima"
c.tempo_atendimento = -30
c.tempo_atendimento = "vinte"

#Demonstração de como ficou depois:
print(c)
print()
print()

#Questão B10 (criar lista)
chamados = [
    Chamado("Lentidão nas planilhas", "Humberto", BAIXA, RESOLVIDO, 2),
    Chamado("Sistema caiu", "Gleison", ALTA, ATENDIMENTO, 10),
    Chamado("Impressora", "Eliza", MEDIA, ABERTO, 3),
    Chamado("Rede lenta", "Mizael", ALTA, RESOLVIDO, 8),
    Chamado("E-mail", "Raulino", BAIXA, ABERTO, 1),
    Chamado("Trocar senha", "Felipe", MEDIA, ABERTO, 5),
    Chamado("Erro de login", "Pedro", ALTA, RESOLVIDO, 7)
]

print("QUESTÃO B10".center(50, "."))
print()
print("LISTA DE CHAMADOS".center(20))
for chamado in chamados:
    print(chamado)

resolvidos = sum(1 for c in chamados if c.esta_resolvido())
total_horas = sum(c.tempo_atendimento for c in chamados)
total_minutos = sum(c.minutos_gastos for c in chamados)

print()
print("." * 50)
print()
print("Resolvidos:", resolvidos)
print("Total de horas:", total_horas)
print("Total de minutos:", total_minutos)
