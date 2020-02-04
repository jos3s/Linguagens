from datetime import date
atual=date.today().year
nasc=int(input('Digite o seu ano de nascimento: '))
idade=atual-nasc

if idade<18:
    alistamento= (18-idade)+atual
    print('Você está livre')
    print('Você tem {} anos e vai precisar se alistar em {}'.format(idade,alistamento))
elif idade==18:
    print('Você precisa fazer o alistamento')
else:
    print('Você já deveria ter feito o alistamento')
    