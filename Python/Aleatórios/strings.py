cores = {'limpar':'\033[m',
         'azul': '\033[34m',
         'pb': '\033[7:30m'}

nome=str(input('Digite o seu nome:')).strip()
print("Analisando...")
print('Seu nome em maiuscula é: {}' .format(nome.upper()))
print('Seu nome em minuscula é: {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
n=nome.split()
print('Seu primeiro nome é: {}{}{}' .format(cores['azul'],n[0],cores['limpar']))
print('Seu ultimo nome é: {}' .format(n[len(n)-1]))

