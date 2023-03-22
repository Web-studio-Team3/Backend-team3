from pymongo import MongoClient
from pymongo.database import Database

connection = MongoClient("mongodb://localhost:27017")
database = connection["baraholka"]
