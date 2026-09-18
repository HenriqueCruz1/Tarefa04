""" Escreva um programa para ler o número de lados (NumLados) de um polígono regular e a medida 
do lado (MedLado)
Se o número de lados for igual a 3 imprima “TRIÂNGULO”, calcule e mostre a área do triângulo (Use 
o Teorema de HERON para calcular a área do triangulo somente com lados, pesquise no google)
Se o número de lados for igual a 4 imprima “QUADRADO”, calcule e mostre a área do quadrado. 
Se o número de lados for igual a 5 imprime “PENTÁGONO”, calcule e mostre a área do pentágono. 
(Pesquise no google com se calcula a area de um PENTAGONO)
Acrescente as seguintes mensagens ao exercício 1 conforme o caso.
Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO. 
"""

NumLados = int(input("Digite o número de lados da figura a ser analisada: "))

if NumLados == 3:
    print("TRIÂNGULO")
elif NumLados == 4:
    print("QUADRADO")
elif NumLados == 5:
    print("PENTÂGONO")
elif NumLados < 3:
    print("NÃO É UM POLÍGONO")
elif NumLados > 5:
    print("POLÍGONO NÃO IDENTIFICADO")