
from urllib.parse import urlparse

url = 'https://www.google.com/search?q=mozilla+firefox&oq=mozi&aqs=chrome.0.0i433i512l2j0i512j0i433i512j0i512j0i433i512j0i512j69i57j0i512l2.1287j0j4&sourceid=chrome&ie=UTF-8'
partes = urlparse(url)

print('Protocolo:', partes.scheme)     # https
print('Domínio:', partes.netloc)       # www.exemplo.com:8080
print('Caminho:', partes.path)         # /caminho/pagina
print('Parâmetros:', partes.query)      # param=1
print('Âncora:', partes.fragment)       # ancora

print('URLparse',partes)