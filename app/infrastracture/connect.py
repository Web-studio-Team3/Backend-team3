from envparse import Env
from pymongo import MongoClient

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017")

connection = MongoClient(MONGODB_URL)
database = connection["baraholka"]

