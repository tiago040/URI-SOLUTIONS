'''
Evergreen Bushy, um dos duendes ajudantes de Noel, responsável por inventar muitos dos brinquedos distribuídos por Noel e também 
muito conhecido por fazer pegadinhas com o bom velhinho, aprontou mais uma neste ano. 

Como sempre faz todos os anos, Bushy separou os presentes para cada criança colocando um bilhete com o nome dela. O problema que 
ele não se limitou a simplesmente colocar o nome correto da criança no presente: ele zoou :) cada um dos nomes misturando as letras 
segundo uma sequência: duas letras do nome, seguidas por duas letras do sobrenome, seguidas por duas letras do nome e por duas letras 
do sobrenome e assim por diante.

Bem, como Noel está bem cansado e sem tempo para brincadeiras, pediu a você que é expert em programação para fazer um programa que 
converta o nome misturado por Evergreen no nome correto de cada criança.

Apenas um fato curioso: a primeira linha do nome misturado sempre terá um número par de caracteres e a segunda linha, sempre terá 
o mesmo número de caracteres da primeira linha ou um caractere a menos do que a primeira linha.

Entrada
A entrada contém um inteiro N (N < 2000) que indica a quantidade de casos de teste. Cada caso de teste é composto por duas linhas, 
com no máximo 100 caracteres cada. Estas duas linhas contém o nome que foi misturado por Evergreen Bushy, que é composto basicamente 
por letras maiúsculas, minúsculas e espaços em branco.

Saída
Com base nas duas linhas de entrada, você deve imprimir o nome correto da criança, seguindo a regra para decifrá-lo conforme descrição acima.
'''

N = int(input())
for _ in range(N):
    string_1 = list(input())
    string_2 = list(input())
    nome = ''
    while True:
        if len(string_1) == 0:
            if len(string_2) != 0:
                nome += ''.join(string_2[0])
            break
        nome += ''.join(string_1[:2])
        del string_1[:2]
        nome += ''.join(string_2[:2])
        del string_2[:2]
    print(nome)