import mysql.connector

# ─────────────────────────────────────────────────────────
# Day 5 — Mini Project: Python and SQL Integration
# Employee Management Report System using EMP–DEPT schema
# ─────────────────────────────────────────────────────────

# Establish connection to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLTraining@2026"
)

cursor = conn.cursor()
print("Connected to MySQL Server successfully!")

# ─── Step 1: Create and select database ───────────────────
cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
cursor.execute("USE employee_db")
print("Database 'employee_db' selected!")

# ─── Step 2: Create tables ─────────────────────────────────
cursor.execute("DROP TABLE IF EXISTS emp")
cursor.execute("DROP TABLE IF EXISTS dept")

cursor.execute("""
CREATE TABLE dept (
    deptno INT PRIMARY KEY,
    dname  VARCHAR(50),
    loc    VARCHAR(50)
)
""")
print("Table 'dept' created!")

cursor.execute("""
CREATE TABLE emp (
    empno    INT PRIMARY KEY,
    ename    VARCHAR(50),
    job      VARCHAR(50),
    mgr      INT,
    hiredate DATE,
    sal      DECIMAL(10, 2),
    comm     DECIMAL(10, 2),
    deptno   INT,
    FOREIGN KEY (deptno) REFERENCES dept(deptno)
)
""")
print("Table 'emp' created!")

# ─── Step 3: Insert sample data ────────────────────────────
dept_data = [
    (10, 'ACCOUNTING', 'NEW YORK'),
    (20, 'RESEARCH',   'DALLAS'),
    (30, 'SALES',      'CHICAGO'),
    (40, 'OPERATIONS', 'BOSTON')
]
cursor.executemany("INSERT INTO dept VALUES (%s, %s, %s)", dept_data)
conn.commit()
print(f"{cursor.rowcount} department records inserted!")

emp_data = [
    (7369, 'SMITH',  'CLERK',     7902, '1980-12-17', 800.00,  None,    20),
    (7499, 'ALLEN',  'SALESMAN',  7698, '1981-02-20', 1600.00, 300.00,  30),
    (7521, 'WARD',   'SALESMAN',  7698, '1981-02-22', 1250.00, 500.00,  30),
    (7566, 'JONES',  'MANAGER',   7839, '1981-04-02', 2975.00, None,    20),
    (7654, 'MARTIN', 'SALESMAN',  7698, '1981-09-28', 1250.00, 1400.00, 30),
    (7698, 'BLAKE',  'MANAGER',   7839, '1981-05-01', 2850.00, None,    30),
    (7782, 'CLARK',  'MANAGER',   7839, '1981-06-09', 2450.00, None,    10),
    (7788, 'SCOTT',  'ANALYST',   7566, '1987-07-13', 3000.00, None,    20),
    (7839, 'KING',   'PRESIDENT', None, '1981-11-17', 5000.00, None,    10),
    (7844, 'TURNER', 'SALESMAN',  7698, '1981-09-08', 1500.00, 0.00,    30),
    (7876, 'ADAMS',  'CLERK',     7788, '1987-07-13', 1100.00, None,    20),
    (7900, 'JAMES',  'CLERK',     7698, '1981-12-03', 950.00,  None,    30),
    (7902, 'FORD',   'ANALYST',   7566, '1981-12-03', 3000.00, None,    20),
    (7934, 'MILLER', 'CLERK',     7782, '1982-01-23', 1300.00, None,    10)
]

emp_insert_query = """
INSERT INTO emp (empno, ename, job, mgr, hiredate, sal, comm, deptno)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
cursor.executemany(emp_insert_query, emp_data)
conn.commit()
print(f"{cursor.rowcount} employee records inserted!")

# ─── Step 4: Data Exploration ──────────────────────────────
cursor.execute("SELECT * FROM dept")
print("\n=== DEPT Table ===")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT empno, ename, job, sal, deptno FROM emp")
print("\n=== EMP Table (selected columns) ===")
for row in cursor.fetchall():
    print(row)

# ─── Step 5: Report 1 — Department Headcount ───────────────
cursor.execute("""
SELECT d.dname, COUNT(e.empno) AS headcount
FROM dept d
LEFT JOIN emp e ON d.deptno = e.deptno
GROUP BY d.dname
ORDER BY headcount DESC
""")

print("\n--- Report 1: Department Headcount ---")
print(f"{'Department':<15} {'Headcount':>10}")
print("-" * 27)
for row in cursor.fetchall():
    print(f"{row[0]:<15} {row[1]:>10}")

# ─── Step 6: Report 2 — Salary Analysis by Department ──────
cursor.execute("""
SELECT d.dname,
       SUM(e.sal)            AS total_sal,
       ROUND(AVG(e.sal), 2)  AS avg_sal,
       MIN(e.sal)            AS min_sal,
       MAX(e.sal)            AS max_sal
FROM dept d
JOIN emp e ON d.deptno = e.deptno
GROUP BY d.dname
ORDER BY total_sal DESC
""")

print("\n--- Report 2: Salary Analysis by Department ---")
print(f"{'Department':<15} {'Total':>10} {'Average':>10} {'Min':>8} {'Max':>8}")
print("-" * 55)
for row in cursor.fetchall():
    print(f"{row[0]:<15} {float(row[1]):>10.2f} {float(row[2]):>10.2f} {float(row[3]):>8.2f} {float(row[4]):>8.2f}")

# ─── Step 7: Report 3 — Top Earning Employees ──────────────
cursor.execute("""
SELECT e.ename, e.job, e.sal, d.dname
FROM emp e
JOIN dept d ON e.deptno = d.deptno
ORDER BY e.sal DESC
LIMIT 5
""")

print("\n--- Report 3: Top 5 Earning Employees ---")
print(f"{'Name':<10} {'Job':<12} {'Salary':>10} {'Department':<15}")
print("-" * 50)
for row in cursor.fetchall():
    print(f"{row[0]:<10} {row[1]:<12} {float(row[2]):>10.2f} {row[3]:<15}")

# ─── Step 8: Report 4 — Employees Above Average Salary ─────
cursor.execute("""
SELECT e.ename, e.job, e.sal
FROM emp e
WHERE e.sal > (SELECT AVG(sal) FROM emp)
ORDER BY e.sal DESC
""")

rows = cursor.fetchall()
print("\n--- Report 4: Employees Above Average Salary ---")
print(f"{'Name':<10} {'Job':<12} {'Salary':>10}")
print("-" * 35)
for row in rows:
    print(f"{row[0]:<10} {row[1]:<12} {float(row[2]):>10.2f}")
print(f"\nTotal: {len(rows)} employees earn above average.")

# ─── Step 9: Reusable Query Function ───────────────────────
def run_report(cursor, title, query):
    """Execute a SQL query and print results with a formatted title."""
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")
    if rows:
        for row in rows:
            print("  " + " | ".join(str(col) for col in row))
    else:
        print("  No records found.")
    return rows


# Job-wise average salary using the reusable function
run_report(
    cursor,
    "Job-wise Average Salary",
    """
    SELECT job, ROUND(AVG(sal), 2) AS avg_sal
    FROM emp
    GROUP BY job
    ORDER BY avg_sal DESC
    """
)

# ─── Step 10: Final Summary Report ─────────────────────────
cursor.execute("SELECT COUNT(*), ROUND(AVG(sal), 2), MIN(sal), MAX(sal) FROM emp")
stats = cursor.fetchone()

print("\n" + "=" * 60)
print("       EMPLOYEE MANAGEMENT SYSTEM — FINAL REPORT")
print("=" * 60)
print(f"  Total Employees  : {stats[0]}")
print(f"  Average Salary   : {float(stats[1]):>10.2f}")
print(f"  Lowest  Salary   : {float(stats[2]):>10.2f}")
print(f"  Highest Salary   : {float(stats[3]):>10.2f}")
print("=" * 60)

cursor.execute("""
SELECT e.empno, e.ename, e.job, e.sal, d.dname, d.loc
FROM emp e
JOIN dept d ON e.deptno = d.deptno
ORDER BY d.dname, e.sal DESC
""")

print(f"\n{'EmpNo':<8} {'Name':<10} {'Job':<12} {'Salary':>9} {'Dept':<12} {'Location'}")
print("-" * 65)
for row in cursor.fetchall():
    print(f"{row[0]:<8} {row[1]:<10} {row[2]:<12} {float(row[3]):>9.2f} {row[4]:<12} {row[5]}")
print("=" * 60)
print("  End of Report")
print("=" * 60)

# ─── Cleanup ───────────────────────────────────────────────
cursor.close()
conn.close()
print("\nConnection closed.")
