import requests, json

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
    print(f"Titulo: {filme['Title']}")
    print(f"Ano: {filme['Year']}")
    print(f"Duração: {filme['Runtime']}")
    print(f"Linguagem: {filme['Language']}")
    print(f"País: {filme['Country']}")
    print(f"Gêneros: {filme['Genre']}")
    print(f"Diretor: {filme['Director']}")
    print(f"Atores: {filme['Actors']}")
    print(f"Nota IMDB: {filme['imdbRating']}")
    print(f"Premios: {filme['Awards']}")
    op=input('Deseja ver o plot do filme? [Y/N] ')
    if op in 'Yy':
        print(f"Plot: {filme['Plot']}")
    op=input('Deseja ver as notas do filme? [Y/N] ')
    if op in 'Yy':
        for s in filme['Ratings']:
             print(f"{s['Source']}: {s['Value']}")
                   
while True:
    op=input("\nDigite o nome do filme ou SAIR para encerrar: ").upper()
    if op in 'SAIR':
        print(f'Saindo...')
        break
    else:
        tipo=int(input("Você deseja buscar sobre o que?\n1 Movie(Valor padrão) \n2 Series \n3 Episode\nSua escolha: "))
        if tipo ==2:
            filme=buscar(op, "series")
        elif tipo==3:
            filme=buscar(op, "episode")
        else:
            filme=buscar(op)

        if filme['Response']=='False':
            print('Não encontrado')
        else:
            imprimir(filme)