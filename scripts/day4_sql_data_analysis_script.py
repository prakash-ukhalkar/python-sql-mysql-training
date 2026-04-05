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

# 1) Aggregate analysis
cursor.execute("""
SELECT AVG(amount) FROM sales
""")
result = cursor.fetchone()
print("\nAverage Sale Amount:\n")
print(result[0])

# 2) Region-wise group analysis
cursor.execute("""
SELECT region, SUM(amount)
FROM sales
GROUP BY region
""")
print("\nRegion-wise Total Sales:\n")
for row in cursor.fetchall():
    print(row)

# 3) Statistical analysis (Standard Deviation)
cursor.execute("""
SELECT STDDEV(amount)
FROM sales
""")
result = cursor.fetchone()
print("\nStandard Deviation of Sales:\n")
print(result[0])

# 4) Outlier detection
cursor.execute("""
SELECT *
FROM sales
WHERE amount >
(SELECT AVG(amount) + 3*STDDEV(amount) FROM sales)
""")
outliers = cursor.fetchall()
print("\nOutlier Detection (amount > AVG + 3*STDDEV):\n")
if outliers:
    for row in outliers:
        print(row)
else:
    print("No outliers detected.")

cursor.close()
connection.close()
