import random
user_win = 0
pc_win = 0

while True:
    user = int(input('Digite um valor: '))

    parimpar = ' '
    while parimpar not in 'PI':
        parimpar = str(input('Par ou Ímpar: [P/I] ')).strip().upper()[0]

    if parimpar == 'P':
        parimpar_pc = 'I'
        print('O user escolher PAR.')

    elif parimpar == 'I':
        parimpar_pc = 'P'
        print('O user escolheu ÍMPAR.')
    
    pc = random.randint(0, 10)
    soma = user + pc

    print(f'O user jogou {user} e pc jogou {pc}. A soma foi {soma}')


    #PAR OU IPAR // USER E PC
    pi = soma % 2
    print('Deu PAR!' if pi == 0 else 'Deu ÍMPAR!')

    if parimpar == 'P':
        if pi == 0:
            print('O user venceu, ele escolheu PAR.')
            user_win = user_win + 1
        else:
            print('O user perdeu, ele escolheu PAR.')
            pc_win = pc_win + 1
            break
    elif parimpar == 'I':
        if pi == 1:
            print('O user venceu, ele escolheu ÍMPAR.')
            user_win = user_win + 1
        else:
            print('O user perdeu, ele escolheu ÍMPAR.')
            pc_win = pc_win + 1
            break
    print('Vamos jogar de novo...')

print(f'ACABOU. O user venceu {user_win} vezes. ')