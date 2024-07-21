from unittest import skip
import requests
from lxml import html
import pandas as pd
import time
import csv


# URL для запроса данных
url = 'https://en.wikipedia.org/wiki/Wikipedia:List_of_Wikipedias'

# Заголовки запроса, включая строку агента пользователя
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:

# Отправка HTTP GET запроса на целевой URL с указанным заголовком
    response = requests.get(url, headers=headers)

# Парсинг HTML-содержимого ответа с помощью библиотеки lxml
    tree = html.fromstring(response.content)
    
# XPath для выбора интересующих нас данных таблицы
    languages = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[1]//text()')
    articles = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[3]//text()')
    pages = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[4]//text()')
    edits = tree.xpath('//table[contains(@class,"wikitable")]/tbody/tr/td[5]//text()')    

# Сохранение извлекаемых данных в словарь
    data = {
        'Languages' : languages,
        'Articles' : articles,
        'Pages' : pages,
        'Edits' : edits
    }
# Задержка для соблюдения этических норм    
    time.sleep(5)

# Проверки
except requests.HTTPError as e:
    print(f"Ошибка запроса HTTP: {e}")
except requests.RequestException as e:
    print(f"Ошибка запроса: {e}")
except Exception as e:
    print(f"Ошибка: {e}")

# Сохранение данных в CSV с помощью pandas
df = pd.DataFrame(data)
df = df.head(-1) # Удаляем последнюю строку с итогами
df.to_csv('List_of_Wikies_pd.csv', index = False)
#print(df.head(20)) # Проверка первых 20 строк т.к. были сомнения в корректности записей


# Сохранение данных в CSV с помощью csv
data_zip = zip(languages, articles, pages, edits) # Создаем кортеж из списков т.к. длинна списков одинаковая
with open('List_of_Wikies_csv.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Languages', 'Articles', 'Pages', 'Edits'])  # Задаем заголовки столбцов
        csvwriter.writerows(data_zip)