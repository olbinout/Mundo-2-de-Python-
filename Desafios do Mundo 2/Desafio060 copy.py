import math

numero = int(input('DIGITE UM NÚMERO PARA QUE EU POSSA LHE DIZER O FATORIAL DELE: '))
fatorial = math.factorial(numero)
for c in range(numero, 0, -1):
    print(f'{c} ', end = '')
    if c > 1:
        print('* ', end = '')
    else:
        print('= ', end = '')

print(f'{fatorial}')