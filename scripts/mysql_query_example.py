import mysql.connector

# Establish connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLTraining@2026",
    database="training_db"
)

print("Connected to MySQL 'training_db' database successfully!")

cursor = connection.cursor()

# Execute query
cursor.execute("SELECT * FROM students")

print("\nStudent Records:\n")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()