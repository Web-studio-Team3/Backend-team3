from pymongo import MongoClient
from pymongo.database import Database

connection = MongoClient("mongodb://localhost:27017")
database = connection["baraholka"]


def create_database() -> Database:
    yield MongoClient("mongodb://localhost:27017")["fastapi_auth_test3"]
