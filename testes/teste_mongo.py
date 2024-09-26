import pymongo
from books.spiders.book import BookSpider

client = pymongo.MongoClient("mongodb://local:27017")
db = client["book_db"]
print(db.list_collection_names())
client.close()