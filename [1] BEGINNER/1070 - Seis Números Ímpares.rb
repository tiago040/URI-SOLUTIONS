=begin
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
=end

n = gets.chomp.to_i
count = 0
while count < 6
    if n % 2 != 0
        puts n 
        count += 1
    end
    n += 1
end