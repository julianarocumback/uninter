# Nodo
class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None


# Lista encadeada simples
class ListaEncadeada:
    def __init__(self):
        self.head = None

    # Inserir na lista encadeada
    def inserir(self, sigla, nome_estado):
        novo_nodo = Nodo(sigla, nome_estado)
        if self.head == None:
            self.head = novo_nodo
        else:
            novo_nodo.proximo = self.head
            self.head = novo_nodo

    # Mostrar os dados da lista
    def imprimir(self):
        nodo_atual = self.head
        while nodo_atual:
            print(f"{nodo_atual.sigla}", end=" -> ")
            nodo_atual = nodo_atual.proximo


# Tabela hash
class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.tabela = [ListaEncadeada() for i in range(0, self.tamanho)]

    # Função hash
    def FuncaoHash(self, chave):
        if chave == "DF":
            return 7
        else:
            chave = list(chave)
            return (ord(chave[0]) + ord(chave[1])) % self.tamanho

    # Inserir na tabela hash
    def inserir(self, chave, nome_estado):
        posicao = self.FuncaoHash(chave)
        self.tabela[posicao].inserir(chave, nome_estado)

    # Mostrar os dados da tabela
    def imprimir(self):
        for i in range(0, self.tamanho):
            print(end=f"{i}: ")
            print(f"{self.tabela[i].imprimir()}")

           

# Programa principal
estados = TabelaHash()

while True:
    escolha = int(input("\n┌──────────── OPÇÕES ────────────┐"
                        "\n├────────────────────────────────┤"
                        "\n│ [1] Adicionar estados          │"
                        "\n│ [2] Mostrar estados            │"
                        "\n│ [3] Sair                       │"
                        "\n└────────────────────────────────┘"
                        "\n>> "))

    if escolha == 1:
        estados.inserir("AC", "Acre")
        estados.inserir("AL", "Alagoas")
        estados.inserir("AP", "Amapá")
        estados.inserir("AM", "Amazonas")
        estados.inserir("BA", "Bahia")
        estados.inserir("CE", "Ceará")
        estados.inserir("DF", "Distrito Federal")
        estados.inserir("ES", "Espírito Santo")
        estados.inserir("GO", "Goiás")
        estados.inserir("MA", "Maranhão")
        estados.inserir("MT", "Mato Grosso")
        estados.inserir("MS", "Mato Grosso do Sul")
        estados.inserir("MG", "Minas Gerais")
        estados.inserir("PA", "Pará")
        estados.inserir("PB", "Paraíba")
        estados.inserir("PR", "Paraná")
        estados.inserir("PE", "Pernambuco")
        estados.inserir("PI", "Piauí")
        estados.inserir("RJ", "Rio de Janeiro")
        estados.inserir("RN", "Rio Grande do Norte")
        estados.inserir("RS", "Rio Grande do Sul")
        estados.inserir("RO", "Rondônia")
        estados.inserir("RR", "Roraima")
        estados.inserir("SC", "Santa Catarina")
        estados.inserir("SP", "São Paulo")
        estados.inserir("SE", "Sergipe")
        estados.inserir("TO", "Tocantins")
        estados.inserir("JR", "Juliana Theodoro Rocumback")

        print("\n┌────────────────────────────────┐"
              "\n│      Estados adicionados!      │"
              "\n└────────────────────────────────┘")


    elif escolha == 2:
        estados.imprimir()

    elif escolha == 3:
        print("\n┌────────────────────────────────┐"
              "\n│           Finalizado           │"
              "\n└────────────────────────────────┘")
        break

    else:
        print("\n┌────────────────────────────────┐"
              "\n│         Opção inválida         │"
              "\n└────────────────────────────────┘")