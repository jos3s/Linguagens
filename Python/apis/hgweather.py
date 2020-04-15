import requests, json
from time import sleep

def requeste(city,uf):
    request=requests.get(f"https://api.hgbrasil.com/weather?key=a8964320&city_name={city},{uf}&locale=pt")
    dado=json.loads(request.text)
    return dado['results']

def imprimirSemana(dado):
    cont=7
    for value in dado['forecast']:
        print('------------------')
        print(f"Data: {value['date']}, {value['weekday']}")
        print(f"Temperatura: {value['min']}°C min e {value['max']}°C max")
        print(f"Condição: {value['description']}")
        sleep(1.5)
        cont-=1
        if cont==0:
            break

def imprimir(dado):
    print()
    print(f"Cidade: {dado['city_name']}")
    print(f"Data: {dado['date']}")
    print(f"Horário: {dado['time']}")
    print(f"Temperatura: {dado['temp']}°C")
    print(f"Condição: {dado['description']}")
    

    op=input('Deseja ver os horários do nascer e pôr-do-sol?[Y/N] ')
    if op in 'Yy':
        print(f"Nascer do sol: {dado['sunrise']}")
        print(f"Pôr do sol: {dado['sunset']}")

    op=input('Deseja ver a previsão para os póximos 7 dias?[Y/N] ')
    if op in 'Yy':
        imprimirSemana(dado)

while True:
    print()
    op=input("Digite SAIR para encerrar o programa ou nome da cidade: ").lower()
    if op in 'sair':
        print(f'Saindo....')
        sleep(1)
        break
    city=op.lower().title()
    state=input('Digite a sigla do estado: ').upper()
    cidade=requeste(city,state)
    imprimir(cidade)
