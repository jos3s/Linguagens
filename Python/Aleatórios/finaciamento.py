valor=float(input('Digite o valor da casa: '))
salario=float(input('Digite o seu salário:'))
anos=int(input('Digite a quantidade de anos que você pretende pagar: '))
prestacao=valor/(anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, prestacao))

if prestacao <=salario*0.3:
    print('Você tem condições de comprar essa casa.')
else:
    print('Você não tem condições de comprar essa casa.')
