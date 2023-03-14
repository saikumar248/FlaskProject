from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId


class MongoAPI:
    def __init__(self, db, collection):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db]
        self.collection = self.db[collection]

    def read_all(self):
        data = []
        for document in self.collection.find():
            document['_id'] = str(document['_id'])
            data.append(document)
        return data

    def read(self, query):
        data = []
        for document in self.collection.find(query):
            document['_id'] = str(document['_id'])
            data.append(document)
        return data

    def create(self, document):
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def update(self, query, document):
        result = self.collection.update_one(query, {"$set": document})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

app = Flask(__name__)
mongo = MongoAPI("User", "user")

@app.route("/")
def home():
    return "Welcome to the MongoDB API!"

@app.route("/users", methods=["GET"])
def get_all_documents():
    data = mongo.read_all()
    return jsonify(data)

@app.route("/users", methods=["POST"])
def create_document():
    document = request.get_json()
    user_id = mongo.create(document)
    return jsonify({"_id": user_id})

@app.route("/users/<user_id>", methods=["GET"])
def get_document(user_id):
    query = {"_id": ObjectId(user_id)}
    data = mongo.read(query)
    return jsonify(data)

@app.route("/users/<user_id>", methods=["PUT"])
def update_document(user_id):
    query = {"_id": ObjectId(user_id)}
    document = request.get_json()
    result = mongo.update(query, document)
    return jsonify({"modified_count": result})

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_document(user_id):
    query = {"_id": ObjectId(user_id)}
    result = mongo.delete(query)
    return jsonify({"deleted_count": result})

if __name__ == "__main__":
    app.run(debug=True)
