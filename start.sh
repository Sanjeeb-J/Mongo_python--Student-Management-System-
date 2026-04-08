#!/bin/bash
# ─── Start MongoDB + Flask Web App ──────────────────────────────────────────

echo "🔧 Setting up MongoDB directories..."
sudo mkdir -p /var/lib/mongodb /var/log/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb 2>/dev/null || true

echo "🚀 Starting mongod..."
# Kill any stuck mongod first
sudo pkill mongod 2>/dev/null; sleep 1

# Start mongod in background
sudo mongod --fork \
  --logpath /var/log/mongodb/mongod.log \
  --dbpath /var/lib/mongodb \
  --bind_ip_all 2>/dev/null

# Wait for mongo to be ready
echo "⏳ Waiting for MongoDB to be ready..."
for i in {1..10}; do
  python3 -c "from pymongo import MongoClient; MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=1000).admin.command('ping')" 2>/dev/null && break
  sleep 1
done

echo "✅ MongoDB is running!"
echo ""
echo "🌐 Starting Flask web server..."
echo "   Open http://localhost:5000 in your browser"
echo ""

cd /mnt/c/Users/sanje/Documents/Github/Mongo_python
python3 server.py
