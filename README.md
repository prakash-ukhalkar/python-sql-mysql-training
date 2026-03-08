# SQL and MySQL Training (with Python Integration)

A structured, hands-on training repository for learning relational database concepts, SQL with MySQL, and Python-based database connectivity.

The content is organized for classroom delivery and self-learning, with slide decks, demo scripts, reference assets, and Jupyter notebooks.

## Program Objectives

By the end of this training, participants should be able to:

- Explain core relational database concepts and SQL command categories.
- Install and configure MySQL Server and MySQL Workbench.
- Write SQL queries for data retrieval, filtering, aggregation, and joins.
- Work with subqueries and multi-table analysis patterns.
- Connect Python to MySQL and execute queries programmatically.
- Apply SQL workflows to practical analysis tasks.

## Course Roadmap

| Day | Topics |
| --- | --- |
| Day 1 | Introduction to SQL and MySQL Server |
| Day 2 | SQL Queries: `INSERT`, `SELECT`, and filtering |
| Day 3 | Sorting, aggregation, joins, and subqueries |
| Day 4 | Data analysis using SQL |
| Day 5 | Mini project: Python + SQL integration |

## Repository Structure

```text
SQL_MySQL_Trainings/
|-- datasets/                    # Training datasets (currently empty placeholder)
|-- docs/
|   |-- imgs/                    # Installation reference screenshots
|   |-- day1_sql_mysql_demo_script.docx
|   `-- day1_sql_mysql_demo_script.pdf
|-- images/                      # Additional image assets (currently empty placeholder)
|-- installer/
|   |-- mysql-installer-web-community-8.0.45.0.msi
|   |-- mysql-workbench-community-8.0.46-winx64.msi
|   `-- Port 3306.txt            # Local setup reference values
|-- notebooks/
|   `-- day1_sql_mysql_python_notebook.ipynb
|-- scripts/                     # Optional scripts (currently empty placeholder)
|-- slides/
|   |-- day1_sql_mysql_training.pdf
|   `-- day1_sql_mysql_training.pptx
|-- LICENSE
`-- README.md
```

## Technology Stack

| Tool | Purpose |
| --- | --- |
| Python | Scripting and database integration |
| MySQL Server | Relational database engine |
| MySQL Workbench | GUI for querying and administration |
| Jupyter Notebook | Interactive training and demos |
| `mysql-connector-python` | Python connector for MySQL |

## Setup Guide (Windows)

### 1. Install Python

- Download: https://www.python.org/downloads/
- Verify:

```bash
python --version
```

### 2. Install MySQL Server and Workbench

Use one of the following:

- Official downloads:
  - https://dev.mysql.com/downloads/mysql/
  - https://dev.mysql.com/downloads/workbench/
- Local installers included in `installer/`.

Recommended local configuration for training:

- Host: `localhost`
- Port: `3306`
- User: `root`

### 3. Install Python Dependencies

```bash
pip install mysql-connector-python jupyter
```

## Running the Notebook

1. Start Jupyter:

```bash
jupyter notebook
```

2. Open `notebooks/day1_sql_mysql_python_notebook.ipynb`.
3. Update connection credentials to match your local MySQL setup.

## Python-MySQL Example

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="training_db",
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
```

## Learning Scope

Core topic coverage includes:

- Database fundamentals (DBMS vs RDBMS, relational model)
- SQL syntax, data types, and command categories
- DDL and DML workflows
- Querying with `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, and aggregates
- Joins and subqueries
- Python connectivity and query execution patterns

## Recommended References

- MySQL Documentation: https://dev.mysql.com/doc/
- MySQL Connector/Python: https://dev.mysql.com/doc/connector-python/en/
- Learning SQL by Alan Beaulieu
- SQL in 10 Minutes by Ben Forta
- Database System Concepts by Silberschatz, Korth, and Sudarshan

## Instructor

**Prakash K. Ukhalkar**  
Assistant Professor (MCA)  
Researcher in Data Science and Machine Learning

## Contributing

Contributions are welcome through issues and pull requests. Suggestions for additional exercises, notebooks, and data-driven examples are especially encouraged.

## License

This project is licensed under the MIT License. See `LICENSE` for details.