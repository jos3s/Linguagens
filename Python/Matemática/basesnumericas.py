num=int(input('Digite o numero:'))
print('Escolha a base:\n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal')
esc=int(input('Digite a opção escolhida: '))

if esc==1:
    print('{} covertido para binario é {}' .format(num, bin(num)[2:]))
elif esc==2:
    print('{} covertido para binario é {}' .format(num, oct(num)[2:]))
elif esc==3:
    print('{} covertido para binario é {}' .format(num, hex(num)[2:]))
else:
    print('Escolha inválida')