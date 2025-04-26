print('GERADOR DE PA')
print('=-'*8)

termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

pa = termo1
c = 1

while c <= 10:

    print(f'{pa}', end=' -> ')   
    
    pa = pa + razao
    c = c + 1

print('FIM')
