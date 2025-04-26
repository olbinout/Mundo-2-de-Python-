num = contador = soma = 0

num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    
    soma = (soma + num)
    contador = contador + 1
    
    num = int(input('Digite um número [999 para parar]: '))

print(f'Foram {contador} números digitados.')
print(f'E a soma dos números digitados foi de: {soma}')