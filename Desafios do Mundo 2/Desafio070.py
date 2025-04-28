print('='*40)
print('ATACADÃO DO AROLDO')
print('='*40)

soma = conte_mil = menor_preco = contador = 0
preco_nome = ''

while True:
    produto = str(input('Diga o nome do produto: ')).strip().title()
    preco = float(input('Quanto custou o produto? R$'))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer adicionar mais coisas no carrinho? [S/N] ')).strip().upper()[0]

    contador += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco 
        preco_nome = produto

    if preco > 1000:
        conte_mil += 1
    
    soma += preco 
    if 'N' in opcao:
        break
    else:
        continue

print(f'O total da compra foi {soma}')
print(f'Teve {conte_mil} produto(s) que foi / foram acima de R$1.000,00')
print(f'O nome do produtor com menor preço é: {preco_nome} e custou R${menor_preco}')