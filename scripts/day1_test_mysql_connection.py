import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLTraining@2026",
    database="training_db"
)

print("Connected to MySQL 'training_db' database successfully!")

conn.close()