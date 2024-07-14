import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import json

books_links = []
titles = []

for i in range(50):
    url = 'https://books.toscrape.com/catalogue/category/books_1/page-' + str(i + 1) + '.html'
    response = requests.get(url, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('article', class_='product_pod')
    for item in items:
        books_links.append(item.find('a').get('href'))

#print(books_links[1])

url_joined = []
for link in books_links:
  url_joined.append(urllib.parse.urljoin('https://books.toscrape.com/catalogue/category/books_1/', link))

#print(url_joined[1])

data_list = []

for url in url_joined:
    response = requests.get(url, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, 'html.parser')
    biblioteque = soup.find_all('article', class_='product_page')
    for book in biblioteque:
        try:
            title = book.find("div", class_="col-sm-6 product_main").h1.text
            price = float(book.find("p", class_="price_color").text[1:].replace("£", ""))
            in_stock_str = book.find("p", class_="instock availability").text.strip()
            in_stock = re.search(r"\d+", in_stock_str)
            number_str = in_stock.group()
            number_int = int(number_str)
            description = book.find_all('p')[3].text

            data = {
                'Title' : title,
                'Price' : price,
                'Instock_available' : number_int,
                'Description' : description
            }

            data_list.append(data)
        except:
            print('Your parcing going wrong =(')

with open('biblioteque_books_toscrape.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
