numeros=('Zero', 'Um', 'Dois', 'Tres', 'Quatro','Cinco','Seis','Sete', 'Oito', 'Nove','Dez')
while True:
    num=int(input('Digite um numero: [Entre 0 e 10] '))
    if num <0 or num >10:
        continue
    print(f'O numero digitado foi {numeros[num]}')
