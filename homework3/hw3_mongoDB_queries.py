from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = client["gb_homework"]
collection = database["homeworks"]

count = collection.count_documents({})
print(f"Число записей в БД = {count}")


pipeline = [
    {"$group": {"_id": None, "max_price": {"$max": "$Price"}, "min_price": {"$min": "$Price"}}}
]
result = list(collection.aggregate(pipeline))
max_price = result[0]["max_price"]
min_price = result[0]["min_price"]

expensive_book = collection.find({"Price": {"$gte": max_price}})
for book in expensive_book:
    title_exp = book['Title']
cheep_book = collection.find({"Price": {"$lte": min_price}})
for book1 in cheep_book:
    title_chp = book1['Title']

print(f'Название книги с минимальной ценой в каталоге: {title_chp}. Стоимость: {min_price} £')
print(f'Название книги с минимальной ценой в каталоге: {title_exp}. Стоимость: {max_price} £')

query = {"Instock_available": {"$lte": 0}}
documents = collection.find(query)

count = collection.count_documents(query)
print(f'Количество отсутсвующих на складе книг: {count}')

query_ = {"Price": {"$lte": min_price}}
documents = collection.find(query_)

count_ = collection.count_documents(query_)
print(f'Количество книг с минимальной ценой в каталоге: {count_}')