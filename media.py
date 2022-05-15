# cálculo de média 

i = 0
soma = 0
quant_nota = float(input('Digite a quantidade de notas: '))

while i < quant_nota:
    nota = float(input(f"Digite a nota {i+1}: "))
    soma = soma + nota
    i = i + 1
media = soma / quant_nota

if media >= 7:
    print(f'Aluno aprovado com média {media:.2f}')
elif media < 7 and media >= 4:
    print(f'A média do aluno é {media:.2f}. Exame final!')
else:
    print(f'Aluno reprovado com média {media:.2f}.')