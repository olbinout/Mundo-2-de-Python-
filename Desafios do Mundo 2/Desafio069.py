print('='*40)
print('O CADASTRO ÚNICO DOS CIDADÃOS')

pessoas_com_18 = quant_homens = menos_de_20_mulher = 0

while True:
    print('='*40)
    idade = int(input('Qual a sua idade? '))
    
    if idade > 18:
        print('INFORMAÇÃO IMPORTANTE.')
        pessoas_com_18 += 1

    print('='*40)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
        
        if sexo == 'M':
            print('OUTRA INFORMAÇÃO IMPORTANTE.')
            quant_homens += 1

        elif sexo == 'F' and idade < 20:
            menos_de_20_mulher += 1

    print('='*40)       
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if 'N' in opcao:
        print('Ok, vamos parar por enquanto.')
        break

    elif 'S' in opcao:
        continue

print()
print(f'A) Quantas pessoas tem mais de 18 anos: {pessoas_com_18}')
print(f'B) Quantos homens foram cadastrados: {quant_homens}')
print(f'C) Quantas mulheres tem menos de 20 anos: {menos_de_20_mulher}')
print()
