import requests, json
from textblob import TextBlob
from time import sleep

cores={
    'padrao':'\033[m',
    'azul':'\033[34m',
    'verde':'\033[32m',
    'verm':'\033[31m',
    'amar':'\033[33m',
    'magenta':'\033[35m',
}

def buscar(titulo, tipo=None):
    req=None
    try:
        req=requests.get(f"http://www.omdbapi.com/?i=tt3896198&apikey=cf700c3a&t={titulo}&plot=full&type={ tipo if tipo is not None else ''}")
        dado=json.loads(req.text)
        return dado
    except:
        print("Erro de conexão")
        return None

def imprimir(filme):
    print()
    print(f"{cores['amar']}Titulo: {filme['Title']} {cores['padrao']}")
    print(f"Ano: {filme['Year']}")
    print(f"Duração: {filme['Runtime']}")
    print(f"Linguagem: {filme['Language']}")
    print(f"País: {filme['Country']}")
    print(f"Gêneros: {filme['Genre']}")
    print(f"Diretor: {filme['Director']}")
    print(f"Atores: {filme['Actors']}")
    print(f"Nota IMDB: {filme['imdbRating']}")
    print(f"Premios: {filme['Awards']}")
    print()
    op=input(f'Deseja ver o plot do filme? [Y/N] ')
    if op in 'Yy':
        print(f"{cores['verde']}Plot: {filme['Plot']}{cores['padrao']}")
        op=input('Deseja traduzir o plot do filme? [Y/N] ')
        if op in 'Yy':
            original=TextBlob(filme['Plot'])
            original.detect_language()
            sleep(.2)
            print(f'Tradução: ')
            print(f'{cores["verde"]}{original.translate(to="pt_br")} {cores["padrao"]}')
    print()
    op=input(f'Deseja ver as notas do filme? [Y/N] ')
    if op in 'Yy':
        print(cores["magenta"], end='')
        for s in filme['Ratings']:
            print(f"{s['Source']}: {s['Value']}")
        print(cores['padrao'])

while True:
    op=input(f"{cores['azul']}Digite o nome do filme ou SAIR para encerrar: {cores['padrao']} ").upper()
    if op in 'SAIR':
        print()
        print(f'{cores["verm"]}Saindo...{cores["padrao"]}')
        print()
        break
    else:
        tipo=int(input("Você deseja buscar sobre o que?\n1 Movie(Valor padrão) \n2 Series \n3 Episode\nSua escolha: "))
        if tipo ==2:
            filme=buscar(op, "series")
        elif tipo==3:
            filme=buscar(op, "episode")
        elif tipo==1:
            filme=buscar(op)
        else:
            print('Opção inválida')
        if filme['Response']=='False':
            print('Não encontrado')
        else:
            imprimir(filme)