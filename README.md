# 🎓 Student Management System (MongoDB + Python)

A beautiful, modern, and reactive **Student Management System** built with Python (Flask) and MongoDB. This project covers full CRUD (Create, Read, Update, Delete) operations and was developed as part of **Experiment 18: MongoDB with Python (CRUD)**.

---

## 🎨 Preview & Features

- **Rich Dark UI**: Modern glassmorphic design with vibrant aesthetics.
- **Real-time Stats**: Track total students, departments, unique cities, and average age.
- **Full CRUD Operations**:
  - **Insert**: Add students with name, age, department, and city.
  - **View**: Responsive table with all student records.
  - **Update**: Modal-based editing for existing student data.
  - **Delete**: Remove specific students or clear the entire database.
- **Search & Filter**: Find students by name, department, or city instantly.
- **Quick Demo**: One-click insertion of sample data for testing.

---

## 🛠️ Technology Stack

- **Backend**: Python 3, Flask
- **Database**: MongoDB (8.0+)
- **Frontend**: Semantic HTML5, Vanilla CSS (Glassmorphism), Vanilla JavaScript
- **Environment**: Optimized for WSL (Windows Subsystem for Linux)

---

## 🚀 Getting Started (WSL Instructions)

### 1. Prerequisites
Ensure you have MongoDB and Python installed in your WSL environment.

```bash
# Install Pymongo and Flask (Ubuntu 24.04+)
pip3 install pymongo flask --break-system-packages
```

### 2. Startup Script
Use the provided `start.sh` script to automatically start the MongoDB service and the Flask server.

```bash
# Make the script executable
chmod +x start.sh

# Run the startup script (Enter your sudo password when prompted)
./start.sh
```

### 3. Accessing the App
Once the server is running, open your browser and navigate to:
👉 **[http://localhost:5000](http://localhost:5000)**

---

## 🔬 Experiment 18: Aim & Viva Tips

### 🎯 Aim
To create a simple Student Management System using MongoDB and Python to perform Insert, View, Update, and Delete operations.

### 🧠 Viva Tips
- **What is MongoDB?** A NoSQL document-oriented database that stores data in JSON-like format.
- **What is Pymongo?** A Python library used to interact with MongoDB.
- **SQL vs. MongoDB**: SQL uses tables and rows; MongoDB uses collections and documents.
- **What is `$set`?**: A MongoDB operator used to update specific fields in a document without overwriting the entire record.

---

## 📁 Project Structure

- `server.py`: The Flask backend handling API routes and MongoDB connection.
- `templates/index.html`: The main UI with CSS styling and JavaScript logic.
- `experiment18.py`: The original CLI-based CRUD experiment script.
- `start.sh`: Automation script for starting services.

---

## ✍️ Usage Note
The web application automatically connects to a local MongoDB instance on port `27017` and uses the database `studentDB` and collection `students`.

---
*Created as part of Experiment 18 - MongoDB Python CRUD Experiment.*
