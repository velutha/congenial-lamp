from src import DB

class User():

    def __init__(self, user_id):
        self.collection = DB["users"]
        self.user_id = user_id

    def find(self):
        results = self.collection.find({"user_id": self.user_id})
        return results
