# tabuada utilizando while
from traceback import print_tb

i = 0

numero = int(input("Digite o número desejado para visualizar a tabuada: "))

while i < 10:
    print(f'{numero} X {i + 1} = {numero * (i + 1)}')
    numero + 1
    i += 1




