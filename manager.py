class Manager():

    def __init__(self, db, collection):
        self.db = db
        self.collection = db[collection]

    def get_all(self):
        return self.collection.find()
    
    def get_by_name(self, name):
        return self.collection.find_one({'name': name})
    
    def filter(self, query):
        return self.collection.find(query)
    
    def sort(self, collection, key="name", order=1):
        return collection.find().sort(key, order)

    def insert(self, data):
        self.collection.insert_one(data)
    
    def insert_many(self, data):
        self.collection.insert_many(data)

    def update(self, query, data):
        self.collection.update_one(query, { "$set": data })
    
    def delete(self, query):
        self.collection.delete_many(query)
    