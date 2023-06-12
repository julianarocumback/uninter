# função das dimensões do objeto
def dimensoesObjeto():
    while True:
        try:
            # cálculo para achar o volume do objeto
            comprimento = float(input('Digite o comprimento do objeto (cm): '))
            largura = float(input('Digite a largura do objeto (cm): '))
            altura = float(input('Digite a altura do objeto (cm): '))
            volume = (comprimento * largura * altura)
        except ValueError:
            # mensagem de erro para erro de digitação
            print('Você digitou alguma dimensão com um valor não numérico \n'+
                  'Por favor, digite as dimensões novamente')
            continue
        # valores cobrados por volume
        if (volume < 1000):
            valor = 10.0
        elif (volume >= 1000 and volume < 10000):
            valor = 20.0
        elif (volume >= 10000 and volume < 30000):
            valor = 30.0
        elif (volume >= 30000 and volume < 100000):
            valor = 50.0
        else:
            # mensagem de erro para objeto muito grande
            print('O volume do objeto é (cm³): {:,.2f}' .format(volume))
            print('Não aceitamos objetos com dimensões tão grandes \n'+
                  'Por favor, digite as dimensões novamente')

            continue
        print('O volume do objeto é (cm³): {:,.2f}' .format(volume))
        return valor

# função do peso do objeto
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (kg): '))
        except ValueError:
            # mensagem de erro para erro de digitação
            print('Você digitou o peso com um valor não numérico \n'+
                  'Por favor, digite as dimensões novamente')
            continue
        # cálculo para achar o valor do peso
        if (peso < 0.1):
            valor = peso * 1
        elif (peso >= 0.1 and peso < 1):
            valor = peso * 1.5
        elif (peso >= 1 and peso < 10):
            valor = peso * 2
        elif (peso >= 10 and peso < 30):
            valor = peso * 3
        else:
            # mensagem de erro para objeto muito pesado
            print('Não aceitamos objetos tão pesados')
            print('Por favor, digite o peso novamente')
            continue
        return valor
    
# função da rota
def rotaObjeto():
    while True:
        # rotas
        print('\n'+ 
            '|****|**************** ROTAS ******************| \n'+
            '| SR | São Paulo        -->   Rio de Janeiro   | \n'+
            '| RS | Rio de Janeiro   -->   São Paulo        | \n'+
            '|----|-----------------------------------------| \n'+
            '| MS | Minas Gerais     -->   São Paulo        | \n'+
            '| SM | São Paulo        -->   Minas Gerais     | \n'+
            '|----|-----------------------------------------| \n'+
            '| RM | Rio de Janeiro   -->   Minas Gerais     | \n'+
            '| MR | Minas Gerais     -->   Rio de Janeiro   | \n')

        rota = input('Escolha a rota: ')
        # multiplicadores da rota 
        if(rota == 'SR'):
            return 1
        elif (rota == 'RS'):
            return 1
        elif (rota == 'MS'):
            return 1.2
        elif (rota == 'SM'):
            return 1.2
        elif (rota == 'RM'):
            return 1.5
        elif (rota == 'MR'):
            return 1.5
        else:
            # mensagem de erro para rota inexistente
            print('Essa rota não existe! \n'+
                  'Por favor, digite a rota novamente')
        continue

# programa principal

# identificador pessoal
print('Bem-vindo(a) à Companhia de Logística Juliana Theodoro Rocumback S.A.| RU: 4472052')

# funções
dimensao = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

# valor total
total = (dimensao * peso * rota)
print('O valor total a ser pago é: R$ {:,.2f} (dimensão: {:,.2f} * peso: {:,.2f} * rota: {:,.2f})' .format(total, dimensao, peso, rota))