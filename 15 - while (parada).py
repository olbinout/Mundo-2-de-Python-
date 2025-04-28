termo = soma = 0

while True:
    termo = float(input('Digite um número: '))
    if termo == 999:
        print('VOCÊ DIGITOU O "flag", então não pediremos mais pra digitar um número.')
        break

    soma = soma + termo

print(f'A soma final dos números digitados foram de: {soma}')
