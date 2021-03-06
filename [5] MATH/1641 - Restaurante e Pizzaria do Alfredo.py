'''
Tradicionalmente depois do Local Contest em Louisiana, juízes e participantes vão juntos para seu restaurante favorito, Restaurante e Pizzaria do Alfredo. Os participantes estão realmente famintos após 5 horas de competição. Para pegar suas pizzas o mais rápido possível, eles decidiram pedir uma pizza grande para todos ao invés de várias pizzas pequenas. Eles gostariam de saber se é possível colocar uma pizza grande com formato retangular sobre a superfície de uma mesa redonda de modo que não fiquem partes penduradas na borda da mesa. Como todos estão cansados e famintos, escreva um programa que os ajude!

Entrada
A entrada possui vários casos de teste. Cada caso de teste começa com um número inteiro R, sendo o raio da superfície da mesa onde os participantes estão sentados (1 ≤ R ≤ 1000). Então 2 números inteiros W e L especificando a largura e altura da pizza (1 ≤ W ≤ L ≤ 1000). A entrada termina com R = 0. Caso contrário, 1 ≤ R ≤ 1000. Então seguem 2 números inteiros W e L especificando a largura e o comprimento da pizza, 1 ≤ W ≤ 1000.

Saída
Haverá uma saída para cada caso de teste informando se uma pizza cabe ou não na mesa com seu número do pedido. Uma pizza que toca a borda da mesa sem ultrapassá-la é considerada como válida. Considere o terceiro exemplo como ilustração deste caso.
'''

count = 1
while True:
    entrada = str(input()).split()
    R = int(entrada[0])
    if R == 0:
        break
    W = int(entrada[1])
    L = int(entrada[2])
    diag = ((W ** 2) + (L ** 2)) ** (1/2)
    diametro = R * 2
    if diag <= diametro:
        print('Pizza {} fits on the table.'.format(count))
    else:
        print('Pizza {} does not fit on the table.'.format(count))
    count += 1