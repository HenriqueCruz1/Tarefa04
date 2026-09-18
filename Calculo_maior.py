"""2. Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário 
não informará valores iguais, valores nulos ou valores negativos. """

maior = int

while True:

    valor_A = int(input("Digite o valor A: "))
    valor_B = int(input("Digite o valor B: "))
    valor_C = int(input("Digite o valor C: "))

    if (valor_A > 0 and
        valor_B > 0 and
        valor_C > 0 and
        valor_A != valor_B and
        valor_A != valor_C and
        valor_B != valor_C):

        break

    else:
        print("Valores inválidos. Digite novamente.")

if valor_A > valor_B and valor_A > valor_C:
    maior = valor_A

elif valor_B > valor_A and valor_B > valor_C:
    maior = valor_B

else:
    maior = valor_C

print(f"O maior valor foi o {maior}")


