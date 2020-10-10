'''
Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. 
Esse método usa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes.
Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada de 10, temos a fórmula abaixo.

https://resources.urionlinejudge.com.br/gallery/images/contests/933.png

Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 10.

Entrada
A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições do denominador na fração continuada.

Saída
A saída é o valor aproximado da raiz quadrada com 10 casas decimais.
'''

N = int(input())
resultado = 0; den = 0

for i in range(N):
    if i == 0:
        resultado = 1/6
    else:
        den = resultado + 6
        resultado = 1/den

print(f'{3+resultado:.10f}')
