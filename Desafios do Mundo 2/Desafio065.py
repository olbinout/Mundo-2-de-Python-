resposta = 'S'

soma = contador = maior_num = menor_num = 0

while resposta in 'S':
    num = float(input('Digite um número: '))
    resposta = str(input('Quer continuar? ')).strip().upper()[0]


    soma = soma + num
    contador = contador + 1

    if contador == 1:
        maior_num = menor_num = num
        
    else: 
        if num > maior_num:
            maior_num = num

        elif num < menor_num:
            menor_num = num
 
media_real = soma / contador

print('='*45)
print(f'O maior número digitado foi {maior_num} e \no menor número digitado foi {menor_num}')
print('='*45)
print(f'A média entre os números digitados foi: {media_real:.2f}')
print('='*45)
print(f'A quantidade de números digitados foi: {contador}')
print('='*45)