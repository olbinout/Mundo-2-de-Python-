numero = soma = contador = 0

while True:
    numero = int(input('Digite um número para somar: '))
    if numero == 999:
        print('')
        print('Você digitou a "FLAG", isso siginica que você parou o programa.')
        break

    soma = soma + numero
    contador = contador + 1
    
print('='*40)
print(f'A soma dos {contador} números digitados foi de: {soma}')
print('='*40)