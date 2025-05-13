import requests
from bs4 import BeautifulSoup
import csv

url = 'https://books.toscrape.com/'

resposta = requests.get(url)
resposta.encoding = 'UTF-8'

soup = BeautifulSoup(resposta.text, 'html.parser')
livros = soup.find_all('article', class_='product_pod')

# Criar o arquivo CSV e escrever o cabeçalho
with open('relatorio.csv', 'w', newline='', encoding='UTF-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['titulo', 'preco', 'link'])

    for livro in livros:
        titulo = livro.h3.a['title']
        link = livro.h3.a['href']
        preco = livro.find('p', class_='price_color').text
        link_completo = 'https://books.toscrape.com/' + link
        escritor.writerow([titulo, preco, link_completo])
    print('Relatório gerado com sucesso!')

