'''CÁLCULO DA MÉDIA GEOMÉTRICA: Faça um algoritmo para 
calcular a Média Geométrica entre duas notas. Se o aluno tiver mais 
de 20 faltas, exiba “reprovado por faltas”, se a nota for menor que 3, 
exiba “reprovado por notas”, se o aluno tirar mais que 3 e menor que 5, 
“Aluno de Recuperação”, se o aluno tirar mais que 5 e menos que 6, 
“Aluno de Exame”, se o aluno tirar mais do que 6, “Aluno Aprovado”. 
Cuide para que as notas de entrada assim como as faltas não sejam 
valores negativos. 
'''

while True:
    nota_A = float(input("Digite a primeira nota: "))
    nota_B = float(input("Digite a segunda nota: "))
    quantidade_faltas = int(input("Digite a quantidade de faltas: "))
    media = (nota_A + nota_B) / 2

    if quantidade_faltas > 0 and media > 0:
        break
    else:
        print("Entrada invalida, há valores negativos")

if quantidade_faltas > 20:
    print(f"quantidade de faltas: {quantidade_faltas}, reprovado por faltas")
        
if media <= 3:
    print(f"media: {media}, reprovado por notas")
elif media > 3 and media <= 5:
    print(f"media: {media}, Aluno de Recuperação")
elif media > 5 and media <= 6:
    print(f"media: {media}, Aluno de Exame")
else:
    print(f"media: {media}, Aluno aprovado")


