from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId
import json

app = Flask(__name__)

# ── MongoDB connection ──────────────────────────────────────────────────────
client = MongoClient("mongodb://localhost:27017/")
db = client["studentDB"]
collection = db["students"]


def serialize(doc):
    """Convert MongoDB document to JSON-serializable dict."""
    doc["_id"] = str(doc["_id"])
    return doc


# ── Routes ──────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


# INSERT
@app.route("/api/students", methods=["POST"])
def insert_student():
    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400
    result = collection.insert_one(data)
    return jsonify({"message": "Student inserted!", "id": str(result.inserted_id)}), 201


# VIEW ALL
@app.route("/api/students", methods=["GET"])
def get_students():
    search = request.args.get("search", "")
    query = {}
    if search:
        query = {
            "$or": [
                {"name":       {"$regex": search, "$options": "i"}},
                {"department": {"$regex": search, "$options": "i"}},
                {"city":       {"$regex": search, "$options": "i"}},
            ]
        }
    students = [serialize(s) for s in collection.find(query)]
    return jsonify(students)


# VIEW ONE
@app.route("/api/students/<id>", methods=["GET"])
def get_student(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if not student:
        return jsonify({"error": "Not found"}), 404
    return jsonify(serialize(student))


# UPDATE
@app.route("/api/students/<id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    data.pop("_id", None)          # Remove _id if accidentally sent
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Student updated!"})


# DELETE
@app.route("/api/students/<id>", methods=["DELETE"])
def delete_student(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Student deleted!"})


# DELETE ALL
@app.route("/api/students", methods=["DELETE"])
def delete_all():
    result = collection.delete_many({})
    return jsonify({"message": f"Deleted {result.deleted_count} students."})


if __name__ == "__main__":
    print("🌐 Student Management System running at http://localhost:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)
