print('PROGRAMA DE PA')
print('-=-'*5)

termo1 = int(input('Por qual número deseja começar? '))
razao = int(input('E qual a razão? '))

pa = termo1
c = 0
total = 0
adiciona = 10

while adiciona != 0:
    total = total + adiciona
    while c <= total:

        print(f'{pa}', end=' -> ')

        pa = pa + razao

        c = c + 1

    print('PAUSE')
    adiciona = int(input('Quantos termos a mais você quer ver? '))

print('FINISH')