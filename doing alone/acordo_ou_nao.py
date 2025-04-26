print(' ACORDO OU NÃO? ')

rn_d = int(input('Quantos dias que a criança nasceu? '))

m_ou_f = str(input('A criança é Masculina ou Feminina? [M/F] ')).strip().upper()

if rn_d <= 30 and 'M' in m_ou_f:
    print('Não Acordei!')

elif rn_d  <= 30 and 'F' in m_ou_f:
    print('Acordei.')

else:
    print('Acordei') 