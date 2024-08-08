import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pandas as pd

user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 " 
              "Safari/537.36")

chrome_options = Options()
chrome_options.add_argument(f'user_agent={user_agent}')


driver = webdriver.Chrome(options=chrome_options)

quotes = []

try:
    driver.get("https://ru.citaty.net/")

    pause_time = 2
    
    while True:
        quote_elements = driver.find_elements(By.XPATH, '//article[@class = "quote "]')
        time.sleep(pause_time)
        for quote_element in quote_elements:
            quote = quote_element.find_element(By.XPATH,'.//p[@class = "blockquote-text"]').text
            author = quote_element.find_element(By.XPATH,'.//p[@class = "blockquote-origin"]').text
            likes = int(quote_element.find_element(By.XPATH,'.//span[@class = "like-count"]').text)
            quotes.append({"quote": quote, "author": author, "likes" : likes})
        next_button = driver.find_elements(By.XPATH, '//a[@class = "page-link page-link-next iscroll-next"]')
        if not next_button:
            break    
        next_button[0].click()
        time.sleep(pause_time)

    file = 'quotes.json'
    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(quotes, json_file, ensure_ascii=False, indent=2)    

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()

df = pd.read_json('quotes.csv')
#типы данных
print(df.dtypes)
#20 самых залайканных цитат
print(df.sort_values('likes', ascending=False).head(20))
#сортировка по самым богатым на цитаты авторам
print(df['author'].value_counts())