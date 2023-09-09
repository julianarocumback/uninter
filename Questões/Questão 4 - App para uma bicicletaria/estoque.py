# função para cadastrar peças
def cadastrarPeca(codigo):

    print('\nCódigo do produto: {}' .format(codigo_exclusivo))
    peca = input('Digite o nome da peça: ')
    fabricante = input('Digite o nome do fabricante: ')
    preco = float(input('Digite o valor da peça: R$ '))
    dicionario_peca = {'Código'      : codigo,
                        'Nome'       : peca,
                        'Fabricante' : fabricante,
                        'Preço R$'   : preco}
    estoque.append(dicionario_peca.copy())

# função para consulta de peças
def consultarPeca():
    # menu de consulta
    while True:
        menu_consulta = input('\nMENU DE CONSULTA\n'+
                                '\n'+
                                '1 - Consultar todas as peças \n'+
                                '2 - Consultar peças por código \n'+
                                '3 - Consultar peças por fabricante \n'+
                                '4 - Retornar ao menu principal\n'+
                                '\n'+
                                'Escolha uma opção: ')
        # consulta todas as peças
        if menu_consulta == '1':
            print('Consultar todas as peças')
            for pecas in estoque:
                print(' ')
                for chave, valor in pecas.items():
                    print('{}: {}' .format(chave, valor))
        # consulta por código
        elif menu_consulta == '2':
            print('Consultar peça por código')
            consulta_codigo = int(input('Digite o código da peça: '))
            for pecas in estoque:
                if pecas ['Código'] == consulta_codigo: 
                    print(' ')
                    for chave, valor in pecas.items():
                        print('{}: {}' .format(chave, valor))
        # consulta por fabricante
        elif menu_consulta == '3':
            print('Consultar peça por fabricante')
            consulta_codigo = (input('Digite o nome do fabricante: '))
            for pecas in estoque:
                if pecas ['Fabricante'] == consulta_codigo: 
                    print(' ')
                    for chave, valor in pecas.items():
                        print('{}: {}' .format(chave, valor))
        # retornar ao menu principal
        elif menu_consulta == '4':
            return
        else:
            print('\nCódigo inválido, Por favor digite novamente!\n')
            continue
            

# função para remover peças
def removerPeca():
    print('\nREMOVER PEÇAS\n')  
    consulta_codigo = int(input('Digite o código da peça que deseja remover: '))
    for pecas in estoque:
      if pecas ['Código'] == consulta_codigo: 
        estoque.remove(pecas)
        print('\nO produto foi removido com sucesso!')
    else:
        print('Esse código não existe!')

# programa principal

# identificador pessoal
print('Bem-vindo(a) ao Controle de Estoque da Bicicletaria da Juliana Rocumback S.A. | RU: 4472052')

estoque = []
# Menu principal
codigo_exclusivo = 0
while True:
    menu_principal = input('\nMENU PRINCIPAL\n'+
                            '\n'+
                            '1 - Cadastrar peças \n'+
                            '2 - Consultar peças \n'+
                            '3 - Remover peças \n'+
                            '4 - Sair \n'+
                            '\n'+
                            'Escolha uma opção: ') 
    if menu_principal == '1':
        codigo_exclusivo = codigo_exclusivo + 1  # contador para o código exclusivo
        cadastrarPeca(codigo_exclusivo)
    elif menu_principal == '2':
        consultarPeca()
    elif menu_principal == '3':
        removerPeca()
    elif menu_principal == '4':
        break # encerra o programa
    else:
        print('\nCódigo inválido, Por favor digite novamente!')
        continue # volta ao inicio