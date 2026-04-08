from pymongo import MongoClient

# ─────────────────────────────────────────────
#  Connect to MongoDB
# ─────────────────────────────────────────────
client = MongoClient("mongodb://localhost:27017/")

# Create / use database
db = client["studentDB"]

# Create / use collection
collection = db["students"]

# ─────────────────────────────────────────────
#  1. INSERT DATA
# ─────────────────────────────────────────────
print("=" * 40)
print("STEP 1: INSERTING DATA")
print("=" * 40)

# Insert one student
student1 = {
    "name": "Rahul",
    "age": 20,
    "department": "CSE",
    "city": "Calicut"
}
collection.insert_one(student1)

# Insert multiple students
students = [
    {"name": "Anu",   "age": 21, "department": "ECE", "city": "Kochi"},
    {"name": "Arjun", "age": 22, "department": "ME",  "city": "Kannur"}
]
collection.insert_many(students)

print("Data Inserted Successfully!\n")

# ─────────────────────────────────────────────
#  2. READ / VIEW DATA
# ─────────────────────────────────────────────
print("=" * 40)
print("STEP 2: VIEWING ALL STUDENTS")
print("=" * 40)

for student in collection.find():
    print(student)

print()

# Retrieve specific record
print("Searching for 'Rahul':")
result = collection.find({"name": "Rahul"})
for data in result:
    print(data)

print()

# ─────────────────────────────────────────────
#  3. UPDATE DATA
# ─────────────────────────────────────────────
print("=" * 40)
print("STEP 3: UPDATING DATA")
print("=" * 40)

collection.update_one(
    {"name": "Rahul"},
    {"$set": {"age": 23}}
)
print("Updated Successfully! (Rahul's age changed to 23)")

# Confirm update
print("Rahul after update:")
for data in collection.find({"name": "Rahul"}):
    print(data)

print()

# ─────────────────────────────────────────────
#  4. DELETE DATA
# ─────────────────────────────────────────────
print("=" * 40)
print("STEP 4: DELETING DATA")
print("=" * 40)

# Delete one record
collection.delete_one({"name": "Anu"})
print("Deleted Anu's record.")

# Delete multiple records
collection.delete_many({"city": "Kannur"})
print("Deleted all records with city = Kannur.")

print()

# Show remaining records
print("Remaining Students:")
for student in collection.find():
    print(student)

print()
print("=" * 40)
print("ALL CRUD OPERATIONS COMPLETED!")
print("=" * 40)

# ─────────────────────────────────────────────
#  Cleanup – drop collection so the script can
#  be run multiple times without duplicate data
# ─────────────────────────────────────────────
collection.drop()
print("(Collection dropped for clean re-run)")
