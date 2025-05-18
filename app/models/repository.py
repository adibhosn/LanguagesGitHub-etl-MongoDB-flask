from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDBRepository:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
        self.db = self.client["github_analysis"]
        self.repos_collection = self.db["repositories"]
        self.languages_collection = self.db["languages"]
        self.repos_collection.create_index("id", unique=True)

    def save_repositories(self, repos_data):
        """Salve data without duplicates"""
        for repo in repos_data:
            self.repos_collection.update_one(
                {"id": repo["id"]},  # Using the unique index on "id"
                {"$set": repo},
                upsert=True
            )

    def save_language_stats(self, language_data, owner):
        """Salve statistics of languages overwriting the old ones"""
        self.languages_collection.delete_many({"owner": owner})  # Remove stats antigos desse owner
        self.languages_collection.insert_one({
            "owner": owner,
            "stats": language_data.to_dict('records')
        })

    def get_language_stats(self):
        """get statistics of languages"""
        return list(self.languages_collection.find({}, {'_id': 0}))