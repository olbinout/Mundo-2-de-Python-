while True:

    numero = int(input('Digite um número para ver sua tabuada: '))
    if numero < 0: 
        print('Números do conjunto dos inteiros negativos desligam o programa.')
        break

    multiplicado = 0

    while multiplicado <= 10:

        print(f'{numero:2} x {multiplicado:2} = {numero * multiplicado:2}')

        multiplicado = multiplicado + 1

print('PROGRAMA DESLIGADO.')