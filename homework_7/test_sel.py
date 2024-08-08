import pandas as pd

df = pd.read_json('quotes.csv')
#типы данных
print(df.dtypes)
#20 самых залайканных цитат
print(df.sort_values('likes', ascending=False).head(20))
#сортировка по самым богатым на цитаты авторам
print(df['author'].value_counts())