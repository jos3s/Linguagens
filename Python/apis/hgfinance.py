import requests
from time import sleep

request=requests.get("https://api.hgbrasil.com/finance/quotations?key=bd652b81")
data=request.json()
currencies=('USD','EUR','GBP','ARS','BTC')
for i in currencies:
    dataMoney=data['results']['currencies'][i]
    print('-----------------------')
    print(f"Moeda: {dataMoney['name']}")
    print(f"Compra: {dataMoney['sell']}")
    print(f"Venda: {dataMoney['buy']}")
    print(f"Variação: {dataMoney['variation']}") 
    sleep(2)
