import mysql.connector

# Establish connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLTraining@2026"  # Replace if your local password is different
)

print("Connected to MySQL server successfully!")

cursor = connection.cursor()

# 1) Create and select database
cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
cursor.execute("USE employee_db")
print("Database 'employee_db' is ready.")

# 2) Create DEPT table
cursor.execute("DROP TABLE IF EXISTS dept")
cursor.execute("""
CREATE TABLE dept (
    deptno INT PRIMARY KEY,
    dname VARCHAR(50),
    loc VARCHAR(50)
)
""")
print("Table 'dept' created successfully.")

# 3) Create EMP table
cursor.execute("DROP TABLE IF EXISTS emp")
cursor.execute("""
CREATE TABLE emp (
    empno INT PRIMARY KEY,
    ename VARCHAR(50),
    job VARCHAR(50),
    mgr INT,
    hiredate DATE,
    sal DECIMAL(10,2),
    comm DECIMAL(10,2),
    deptno INT,
    FOREIGN KEY (deptno) REFERENCES dept(deptno)
)
""")
print("Table 'emp' created successfully.")

# 4) Insert DEPT rows
dept_data = [
    (10, "ACCOUNTING", "NEW YORK"),
    (20, "RESEARCH", "DALLAS"),
    (30, "SALES", "CHICAGO"),
    (40, "OPERATIONS", "BOSTON")
]

cursor.executemany("INSERT INTO dept VALUES (%s, %s, %s)", dept_data)
connection.commit()
print("DEPT rows inserted successfully.")

# 5) Insert EMP rows
emp_data = [
    (7369, "SMITH", "CLERK", 7902, "1980-12-17", 800, None, 20),
    (7499, "ALLEN", "SALESMAN", 7698, "1981-02-20", 1600, 300, 30),
    (7521, "WARD", "SALESMAN", 7698, "1981-02-22", 1250, 500, 30),
    (7566, "JONES", "MANAGER", 7839, "1981-04-02", 2975, None, 20),
    (7654, "MARTIN", "SALESMAN", 7698, "1981-09-28", 1250, 1400, 30),
    (7698, "BLAKE", "MANAGER", 7839, "1981-05-01", 2850, None, 30),
    (7782, "CLARK", "MANAGER", 7839, "1981-06-09", 2450, None, 10),
    (7788, "SCOTT", "ANALYST", 7566, "1987-07-13", 3000, None, 20),
    (7839, "KING", "PRESIDENT", None, "1981-11-17", 5000, None, 10),
    (7844, "TURNER", "SALESMAN", 7698, "1981-09-08", 1500, 0, 30),
    (7876, "ADAMS", "CLERK", 7788, "1987-07-13", 1100, None, 20),
    (7900, "JAMES", "CLERK", 7698, "1981-12-03", 950, None, 30),
    (7902, "FORD", "ANALYST", 7566, "1981-12-03", 3000, None, 20),
    (7934, "MILLER", "CLERK", 7782, "1982-01-23", 1300, None, 10)
]

insert_emp_query = """
INSERT INTO emp (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(insert_emp_query, emp_data)
connection.commit()
print("EMP rows inserted successfully.")

# 6) View EMP table
cursor.execute("SELECT * FROM emp")
print("\nEMP Records:\n")
for row in cursor.fetchall():
    print(row)

# 7) Join EMP + DEPT
cursor.execute("""
SELECT e.ename, e.job, d.dname, d.loc
FROM emp e
JOIN dept d ON e.deptno = d.deptno
""")
print("\nEMP + DEPT Join Result:\n")
for row in cursor.fetchall():
    print(row)

# 8) Average salary by department
cursor.execute("""
SELECT deptno, AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
""")
print("\nAverage Salary by Department:\n")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
print("\nConnection closed.")
