'''
A briga continua para decidir se é melhor armazenar números começando pelos seus dígitos mais significativos ou pelos seus dígitos menos significativos. Às vezes ela é chamada de "Endian War". Essa batalha teve início há muito tempo atrás, nos primórdios da Ciência da Computação. Joe Stoy, em seu (a propósito, excelente) livro "Denotational Semantics" ("Semântica Denotacional"), conta a história a seguir:

"A decisão sobre para que lado escrevermos os dígitos é, claro, matematicamente trivial. Entretanto, um dos primeiros computadores britânicos tinha números escritos da direita para a esquerda (porque o feixe de luz de um tubo de osciloscópio vai da direita para a esquerda, mas na lógica serial trata-se primeiro dos dígitos menos significativos). Turing costumava confundir seu público em palestras públicas quando, por acaso, ele entrava neste modo mesmo para aritmética decimal, e escrevia coisas como 73+42=16. A versão seguinte da máquina foi tornada mais convencional simplesmente invertendo os fios da deflexão no eixo X: isso, porém, preocupou os engenheiros, já que suas formas de onda ficaram todas ao contrário. Esse problema, por sua vez, foi resolvido criando uma pequena janela para que os engenheiros (que tendiam a ficar atrás do computador mesmo) pudessem ver a tela do osciloscópio de trás.
[C.Strachey - comunicação privada.]"

Você vai fazer o papel do público e julgar se as equações de Turing são verdadeiras.

Entrada
A entrada contém vários casos de teste. Cada caso especifica em uma única linha uma equação de Turing. Uma equação de Turing tem a forma "a+b=c", onde a, b, c são números compostos de dígitos 0,...,9. Cada número consiste de, no máximo, 7 dígitos. Isso inclui possíveis zeros à esquerda ou à direita. A equação "0+0=0" terminará a entrada e deve ser processada também. As equações não contêm espaços.

Saída
Para cada caso de teste gere uma linha contendo a palavra "True" ou a palavra "False", se a equação é verdadeira ou falsa, respectivamente, na interpretação de Turing, ou seja, com os números escritos de trás para frente.
'''

while True:
    eq = str(input())
    eq_2 = eq
    eq = list(eq)
    eq = ''.join(eq[::-1])
    eq = eq.split(sep='=')
    a = int(eq[0])
    del eq[0]
    eq = ''.join(eq)
    eq = eq.split(sep='+')
    b = int(eq[0])
    c = int(eq[1])
    if b + c == a:
        print('True')
    else:
        print('False')
    if eq_2 == '0+0=0':
        break