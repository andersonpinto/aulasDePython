from urllib import request

url = 'https://www.news.google.com'
response = request.urlopen(url)   # Abre a URL
html = response.read()            # Lê o conteúdo da página
print(html.decode('utf-8'))       # Imprime o conteúdo decodificado para texto
