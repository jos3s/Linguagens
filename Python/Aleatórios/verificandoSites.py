import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Impossível acessar o site')
else:
    print('Foi possível acessar o site')