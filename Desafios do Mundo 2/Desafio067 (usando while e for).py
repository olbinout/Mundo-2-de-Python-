multiplicador = 0


while True:
    termo = int(input('Quer ver a tabuada de qual número? '))
    
    print('='*40)
    if termo < 0:
        print('Números do conjunto dos inteiros negativos desligam o programa.')
        print()
        print('FINALIZADO.')
        break

    for c in range (0, 11):
        print(f'{termo} x {c} = {termo * c}')

    print('='*40)

