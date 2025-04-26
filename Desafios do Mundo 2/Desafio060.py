#CALCULADORA DE FATORIAL:
numero = int(input('DIGITE UM NÚMERO: '))
numero_fatorial = numero
fatorial = 1

print(f'Calculando o fatorial de {numero}')
while numero_fatorial > 0:
    print(f'{numero_fatorial}', end = '')
    if numero_fatorial > 1:
        print(' x ', end = '')
    else:
        print(' = ', end = '')
        
    fatorial = fatorial * numero_fatorial 
    numero_fatorial = numero_fatorial - 1

print(f'{fatorial}.')