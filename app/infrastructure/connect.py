from pymongo import MongoClient
from pymongo.database import Database
from envparse import Env

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017")

connection = MongoClient(MONGODB_URL)
database = connection["baraholka"]