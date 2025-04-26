termos = int(input('Quantos termos da sequência de FIBONACCI você quer ver? '))


c = 3 
ter1 = 0
ter2 = 1
ter3 = ter1 + ter2

print(f'{ter1} -> {ter2}', end=' -> ')
while c <= termos:

    
    print(f'{ter3}', end=' -> ')    
    ter1 = ter2
    ter2 = ter3
    ter3 = ter1 + ter2

    c = c + 1
print('FIM')