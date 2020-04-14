import requests

def main():
    print('Consulta CEP')
    print()

    cep=input('Digite o cep a ser buscado:')
    if len(cep)!=8:
        print("Quantidade de dígitos inválida.")
        exit()

    request=requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    adressData=request.json()
    if 'erro' not in adressData:
        print('\nCEP Encontrado==>')
        print(f"CEP: {adressData['cep']}")
        print(f"Logradouro: {adressData['logradouro']}")
        print(f"Complemento: {adressData['complemento']}")
        print(f"Bairro: {adressData['bairro']}")
        print(f"Cidade: {adressData['localidade']}")
        print(f"UF: {adressData['uf']}")
    else:
        print("CEP Inválido")
        
    opt=input('\nDeseja realizar uma nova consulta? [Y/N] ')
    if opt in 'Yy':
        main()
    else:
        print('Saindo...')

if __name__ =='__main__':
    main()
