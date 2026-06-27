'''import urllib.request

try:
    urllib.request.urlopen('https://pudim.com.br/')
except:
    print('Nesse momento não foi possível acessar o site.')
else:
    print('O site foi acessado e está funcionando!')'''

#fiz o cod igual do prof mas nao ta pegando
#tive que instalar a bilbioteca requests

import requests

try:
    requests.get('https://pudim.com.br/', timeout=5)
except:
    print('Nesse momento não foi possível acessar o site.')
else:
    print('O site foi acessado e está funcionando!')