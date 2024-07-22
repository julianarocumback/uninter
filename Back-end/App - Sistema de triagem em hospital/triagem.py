# Nodo
class Nodo:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None


# Lista encadeada simples
class ListaEncadeada:
    def __init__(self):
        self.head = None

    # Cartão verde
    def inserirSemPrioridade (self):
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = self.novo_nodo

    # Cartão amarelo
    def inserirComPrioridade(self):
        nodo_atual = self.head
        if self.head.cor == "V":
            self.novo_nodo.proximo = self.head
            self.head = self.novo_nodo
        else:
            while nodo_atual.cor != "V":
                self.novo_nodo.proximo = nodo_atual.proximo
                temp = nodo_atual
                if nodo_atual.proximo == None:
                    break
                else:
                    nodo_atual = nodo_atual.proximo
            nodo_atual = temp
            nodo_atual.proximo = self.novo_nodo


    # Opção da cor do cartão
    def inserir(self):
        while True:
            cor = input("\n ┌──────────── CARTÃO ────────────┐"
                        "\n ├────────────────────────────────┤"
                        "\n │ [A] Amarelo                    │"
                        "\n │ [V] Verde                      │"
                        "\n └────────────────────────────────┘"
                        "\n >> ")

            if cor == "A" or cor == "V":
                numero = int(input("\n ┌─────────── NÚMERO ─────────────┐"
                                   "\n ├────────────────────────────────┤"
                                   "\n │   Digite o número do cartão    │"
                                   "\n └────────────────────────────────┘"
                                   "\n >> "))

                if cor == "A" and numero < 201:
                    print("\n ┌──────────────────────────────────────────┐"
                          "\n │ Cartões amarelos começam a partir de 201 │"
                          "\n └──────────────────────────────────────────┘")
                    continue

                elif cor == "V" and numero > 200:
                    print("\n ┌───────────────────────────────────────┐"
                          "\n │ Cartões verdes começam do 1 até o 200 │"
                          "\n └───────────────────────────────────────┘")
                    continue

            else:
                print("\n ┌────────────────────────────────┐"
                      "\n │         Opção inválida         │"
                      "\n └────────────────────────────────┘")
                continue

            # Criar nodo e as opções para adicioná-lo
            self.novo_nodo = Nodo(cor, numero)
            if self.head == None:
                self.head = self.novo_nodo

            elif cor == "A":
                fila.inserirComPrioridade()

            elif cor == "V":
                fila.inserirSemPrioridade()

            print("\n ┌────────────────────────────────┐"
                  "\n │  Paciente adicionado na fila!  │"
                  "\n └────────────────────────────────┘")
            break


    # Mostrar a lista de espera
    def imprimirListaEspera(self):
        nodo_atual = self.head
        print(end=" Lista:")
        while nodo_atual:
            print(f" [{nodo_atual.cor}, {nodo_atual.numero}]", end=" -> ")
            nodo_atual = nodo_atual.proximo
        print("[Fim da fila]")


    # Remover paciente da lista
    def atenderPaciente(self):
        if self.head == None:
            print("\n ┌────────────────────────────────┐"
                  "\n │       A fila está vazia!       │"
                  "\n └────────────────────────────────┘")
        else:

            print(f"\n ┌─────────────────────────────────────────┐"
                  f"\n   O paciente [{self.head.cor},{self.head.numero}] será atendido agora! "
                  f"\n └─────────────────────────────────────────┘")
            self.head = self.head.proximo


# Menu principal
def menu():
    while True:
        escolha = int(input("\n ┌──────────── OPÇÕES ────────────┐"
                            "\n ├────────────────────────────────┤"
                            "\n │ [1] Adicionar paciente a fila  │"
                            "\n │ [2] Mostrar pacientes na fila  │"
                            "\n │ [3] Chamar paciente            │"
                            "\n │ [4] Sair                       │"
                            "\n └────────────────────────────────┘"
                            "\n >> "))

        if escolha == 1:
            fila.inserir()
        elif escolha == 2:
            fila.imprimirListaEspera()
        elif escolha == 3:
            fila.atenderPaciente()
        elif escolha == 4:
            print("\n ┌────────────────────────────────┐"
                  "\n │           Finalizado           │"
                  "\n └────────────────────────────────┘")
            break
        else:
            print("\n ┌────────────────────────────────┐"
                  "\n │         Opção inválida         │"
                  "\n └────────────────────────────────┘")


# programa principal
fila = ListaEncadeada()
menu()