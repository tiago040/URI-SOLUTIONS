{-
Você fica tão feliz no natal que tem vontade de gritar para todo mundo: "Feliz natal!!". Pra colocar toda essa felicidade pra fora, você montou um programa que, colocado um índice I de felicidade, seu grito de natal é mais animado.

Entrada
A entrada é composta por um inteiro I (1 < I ≤ 104) que representa o índice de felicidade.

Saída
A saída é composta pela frase "Feliz natal!", sendo repetidas I vezes a última letra a da frase. Uma quebra de linha é necessária após a impressão da frase.
-}

natal :: Int -> String
natal 1 = "al!"
natal a = "a" ++ natal (a - 1)

main = do
i <- readLn :: IO Int
let resposta = "Feliz nat" ++ natal i
putStrLn resposta