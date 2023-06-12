#identificador pessoal
print('Bem-vindo(a) à Lanchonete da Juliana Theodoro Rocumback | RU: 4472052')

#cardápio
print('')
print('****************** Cardápio ******************')
print('| Código |        Descrição        |   Valor  |')
print('|  100   |    Cachorro Quente      | R$  9,00 |')
print('|  101   |  Cachorro Quente Duplo  | R$ 11,00 |')
print('|  102   |          X-Egg          | R$ 12,00 |')
print('|  103   |        X-Salada         | R$ 13,00 |')
print('|  104   |         X-Bacon         | R$ 14,00 |')
print('|  105   |         X-Tudo          | R$ 17,00 |')
print('|  200   |  Lata de Refrigerante   | R$  5,00 |')
print('|  201   |       Chá Gelado        | R$  4,00 |')
print('')

#escolha do produto
valor = 0
while True:
    codigo = int(input('Digite o código do produto: '))
    if(codigo == 100):
        valor += 9.00
        print('Você pediu um Cachorro Quente no valor de R$ 9,00')
    elif(codigo == 101):
        valor += 11.00
        print('Você pediu um Cachorro Quente Duplo no valor de R$ 11,00')
    elif(codigo == 102):
        valor += 12.00
        print('Você pediu um X-Egg no valor de R$ 12,00')
    elif(codigo == 103):
        valor += 13.00
        print('Você pediu um X-Salada no valor de R$ 13,00')
    elif(codigo == 104):
        valor += 14.00
        print('Você pediu um X-Bacon no valor de R$ 14,00')
    elif(codigo == 105):
        valor += 17.00
        print('Você pediu um X-Tudo no valor de R$ 17,00')
    elif(codigo == 200):
        valor += 5.00
        print('Você pediu uma Lata de Refrigerante no valor de R$ 5,00')
    elif(codigo == 201):
        valor += 4.00
        print('Você pediu um Chá Gelado no valor de R$ 4,00')
    else:
        print('Opção Inválida')
        continue

    #continuar ou não fazendo pedidos
    print('Deseja pedir mais alguma coisa?')
    print('1 - Sim')
    print('0 - Não')
    novopedido = int(input(''))
    if (novopedido == 1):
        continue
    elif (novopedido == 0):
        print('O total a ser pago é: R$ {:.2f}' .format(valor))
        break
    else:
        print('Opção Inválida')