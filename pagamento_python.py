bit=int(input('Digite o bit de verificação:'))
cn='Compra negada'
cs='Compra concluida com sucesso'

if bit==0 :
    valor=int(input('Digite o valor da compra: '))
    if valor<=1000 :
        cartao=input('Digite o numero do cartão: ')
        tam=len(cartao)
        if tam==16:
            senha=int(input('Digite a senha do cartão: '))
            print('\n')
            print('O valor da compra foi {}'.format(valor))
            print('O número do cartão é {}'.format(cartao))
            print(cs)
        else :
            print(cn)
    else :
        print(cn)
else :
    print(cn)
