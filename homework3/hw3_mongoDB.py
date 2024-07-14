from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
database = client["gb_homework"]
collection = database["homeworks"]

with open('biblioteque_books_toscrape.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

collection.insert_many(data)

print(data[0])
