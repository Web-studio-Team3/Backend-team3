from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017")
# db = conn.baraholka
db = conn.Chats
