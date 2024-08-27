from neo4j import GraphDatabase
from pymongo import MongoClient

# MongoDB Integration
class MongoDBDemo:
    def __init__(self, uri, dbname):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        
    def close(self):
        self.client.close()
    
    def add_movie_details(self, movie_details):
        """ Adds detailed movie information to MongoDB """
        collection = self.db["movies"]
        collection.insert_many(movie_details)
    
    def get_movie_details(self, title):
        """ Retrieves movie details from MongoDB by title """
        collection = self.db["movies"]
        return collection.find_one({"title": title})
    
    def add_actor_biographies(self, biographies):
        """ Adds actor biographies to MongoDB """
        collection = self.db["actors"]
        collection.insert_many(biographies)
    
    def get_actor_biography(self, name):
        """ Retrieves actor biography from MongoDB by name """
        collection = self.db["actors"]
        return collection.find_one({"name": name})