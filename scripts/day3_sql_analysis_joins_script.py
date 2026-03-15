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

# 1) Sorting example
cursor.execute("""
SELECT * FROM employees
ORDER BY salary DESC
""")
print("\nEmployees sorted by salary (DESC):\n")
for row in cursor.fetchall():
    print(row)

# 2) Aggregate example
cursor.execute("""
SELECT AVG(salary)
FROM employees
""")
avg_salary = cursor.fetchone()
print("\nAverage salary:\n")
print(avg_salary)

# 3) GROUP BY example
cursor.execute("""
SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id
""")
print("\nDepartment-wise average salary:\n")
for row in cursor.fetchall():
    print(row)

# 4) JOIN example
cursor.execute("""
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id
""")
print("\nEmployees with department names:\n")
for row in cursor.fetchall():
    print(row)

# 5) Subquery example
cursor.execute("""
SELECT name
FROM employees
WHERE salary >
(SELECT AVG(salary) FROM employees)
""")
print("\nEmployees earning more than average salary:\n")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
