### Controle de estoque

**Enunciado:** Imagine que você está desenvolvendo um software de controle de estoque para uma bicicletaria. Este software deve ter o seguinte menu e opções:  

1. Cadastrar Peça
2. Consultar Peça
    1. Consultar Todas as Peças
    2. Consultar Peças por Código
    3. Consultar Peças por Fabricante
    4. Retornar
3. Remover Peça 
4. Sair 

**Elabore um programa em Python que:**

1. Deve-se codificar uma função *cadastrarPeca* (código) **(exigência 1)**;
    * Essa função receberá como parâmetro um código exclusivo para cada peça cadastrado (dica: utilize um contador como parâmetro)
    * Dentro da função, pergunte o nome da peça;
    * Dentro da função, pergunte o fabricante da peça; 
    * Dentro da função, pergunte o valor da peça.
    * Cada peça cadastrada deve ter os seus dados armazenados num *DICIONÁRIO* (dica: Confira o material escrito da p.22 até p.24 da AULA 06) 
2. Deve-se codificar uma função *consultarPeca* **(exigência 2)**; 
    * Dentro da função, deve-se ter um menu com as seguintes opções: 
        * Consultar Todas as Peças 
        * Consultar Peças por Código 
        * Consultar Peças por Fabricante 
        * Retornar 
3. Deve-se codificar uma função chamada *removerPeca* **(exigência 3)**; 
    * Dentro da função, pergunte qual é o código do produto que deseja ser removido do cadastro (da lista de dicionário) 