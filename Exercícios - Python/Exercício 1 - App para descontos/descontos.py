#identificador pessoal
print('Bem-vindo(a) à Loja da Juliana Theodoro Rocumback | RU: 4472052')

#cálculo para achar o valor total
valor_produto = float(input('Digite o valor do produto: R$ '))
quantidade = int(input('Digite a quantidade do produto: '))
valor_total = (valor_produto * quantidade)

#cálculo para achar o desconto de 5%, 10% ou 15% sobre o valor total
desconto_5 = valor_total * (5/100)
desconto_10 = valor_total * (10/100)
desconto_15 = valor_total * (15/100)

#aplicação de desconto de acordo com a quantidade do produto
if(quantidade >= 10 and quantidade <= 99):
    print('O valor total sem desconto é: R$ {:,.2f}' .format(valor_total))
    print('O valor total com desconto é: R$ {:,.2f}' .format(valor_total - desconto_5), '(desconto de 5%)')
elif(quantidade >= 100 and quantidade <= 999):
    print('O valor total sem desconto é: R$ {:,.2f}' .format(valor_total))
    print('O valor total com desconto é: R$ {:,.2f}' .format(valor_total - desconto_10), '(desconto de 10%)')
elif(quantidade >= 1000):
    print('O valor total sem desconto é: R$ {:,.2f}' .format(valor_total))
    print('O valor total com desconto é: R$ {:,.2f}' .format(valor_total - desconto_15), '(desconto de 15%)')
else:
    print('O valor total é: R$ {:,.2f}' .format(valor_total))
