import mysql.connector
from mysql.connector import Error

info = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'port': 3306
}

db_name = "10000CODERS"
table_name = "batch_53r"  # replaced space with underscore

conn = None
cursor = None

try:
    conn = mysql.connector.connect(**info)
    cursor = conn.cursor()
    print("Connected to MySQL server")

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    cursor.execute(f"USE {db_name};")
    print(f"Using database {db_name}")

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100),
        course VARCHAR(100)
    );
    """)
    print(f"Table {table_name} ready")

    cursor.execute(f"TRUNCATE TABLE {table_name};")

    records = [
        ("Aneel", 21, "ane@example.com", "Python"),
        ("sreevani", 23, "sri@example.com", "Web Dev"),
        ("tharun", 22, "nani@example.com", "Data Science"),
        ("sharnya", 24, "sharnya@example.com", "React"),
        ("shannu", 20, "shannu@example.com", "Machine Learning")
    ]
    cursor.executemany(
        f"INSERT INTO {table_name} (name, age, email, course) VALUES (%s, %s, %s, %s)",
        records
    )
    conn.commit()
    print(f"Inserted {cursor.rowcount} records into {table_name}")

    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    print("\nData in table:")
    print("-" * 70)
    print(f"{'ID':<3} {'Name':<10} {'Age':<3} {'Email':<25} {'Course'}")
    print("-" * 70)
    for r in rows:
        print(f"{r[0]:<3} {r[1]:<10} {r[2]:<3} {r[3]:<25} {r[4]}")
    print("-" * 70)

except Error as e:
    print("MySQL error:", e)

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
    print("Connection closed")
    