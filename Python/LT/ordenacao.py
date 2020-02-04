lista = []
while True:
    num=int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print("Adicionado na lista")
    else:
        print('Valor duplicado')
    esc=str(input('Quer continuar: '))
    if esc in 'Nn':
        break
lista.sort()
print(f'Você adicionou: {lista}')

