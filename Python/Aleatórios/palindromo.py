frase=input('Digite a frase: ').strip().upper()
palavras=frase.split()
juncao=''.join(palavras)
inverso=juncao[::-1]
print('A frase é {} ela invertida fica {}'.format(juncao,inverso))
print('A frase {} um palidromo' .format('é' if inverso==juncao else 'não é'))