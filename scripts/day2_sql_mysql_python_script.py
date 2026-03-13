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

# Insert record
cursor.execute("""
INSERT INTO students VALUES
(4, 'Riya', 'MBA', 88)
""")
connection.commit()
print("\nRecord inserted successfully.")

# Retrieve all records
cursor.execute("SELECT * FROM students")
print("\nAll Student Records:\n")
for row in cursor.fetchall():
    print(row)

# Filter records
cursor.execute("""
SELECT name,marks
FROM students
WHERE marks > 80
""")
print("\nStudents with marks > 80:\n")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
