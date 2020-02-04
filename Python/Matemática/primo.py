num = int(input("Digite um número: "))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(i), end='')

print("\n\033[mO número {} foi divisível {} vezes!".format(num, cont))
if cont == 2:
    print("O número é primo")
else:
    print("O número não é primo")