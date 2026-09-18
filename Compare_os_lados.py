""". Escreva um programa que leia o valor de 3 lados inteiros positivos (A,B e C) de um triângulo. 
No início do programa compare os lados para saber se é uma figura de três lados apenas ou se é um 
triângulo, Se qualquer um dos lados for maior ou igual a soma dos outros dois então a figura não é um 
triângulo. SE ( A >= (B+ C) ou B >=(A+C) ou C >= (B+A) ). Se for um triangulo, descubra o TIPO de 
triângulo: “equilátero”, “escaleno” ou “isósceles”. Imprima ao final o TIPO de triângulo. Verifique na 
internet para saber como identificar o TIPO de triângulo

equilátero = todos os lados iguais
isoceles = dois lados iguais e um diferente.
escaleno = todos os lados são diferentes. 
"""

lado_A = int(input("Qual o tamanho do lado A ? "))
lado_B = int(input("Qual o tamanho do lado B ? "))
lado_C = int(input("Qual o tamanho do lado C ? "))

soma_lados = (lado_A + lado_B + lado_C)

if lado_A >= (lado_B + lado_C) or lado_B >= (lado_A + lado_C) or lado_C >= (lado_B + lado_A):
    print("A figura não é um triangulo")

elif lado_A == lado_B and lado_A == lado_C and lado_B == lado_C:
    print("Triangulo equilátero; todos os lados iguais")

elif lado_A != lado_B and lado_B == lado_C or lado_B != lado_C and lado_A == lado_B:
    print("Triangulo isoceles; um dos lados é diferente")

else:
    print("Triangulo escaleno; nenhum dos lados é igual ao outro")
