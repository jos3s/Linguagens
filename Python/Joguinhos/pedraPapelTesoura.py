from random import randint
print("""Escolha:
0 -  Pedra
1 -  Papel
2 - Tesoura""")
jog=int(input('Qual a sua escolha: '))
jogadas=['Pedra','Papel','Tesoura']
comp=randint(0,2)
print('='*21)
print('Você jogou {}'.format(jogadas[jog]))
print('Computador jogou {}' .format(jogadas[comp])) 
print('='*21)
if jog<comp:
    print('O Computador ganhou')
elif jog>comp:
    print('Você ganhou')
else:
    print('Deu empate')

