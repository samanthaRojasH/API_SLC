from flask import Flask
from flask_pymongo import pymongo
#from app import app
import dns
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
CONNECTION_STRING = config['DEFAULT']['CONNECTION_DB']
client = pymongo.MongoClient(CONNECTION_STRING)
                    
db = pymongo.database.Database(client, config['DEFAULT']['DB'])
col = pymongo.collection.Collection(db, config['DEFAULT']['COLLECTION'])