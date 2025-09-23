import sqlite3
import os

DB_FILE = "10000coders.db"

# remove old db for clean start (optional)
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Step 2: create table with email column
cursor.execute('''
CREATE TABLE batch_53r (
    s_no INTEGER PRIMARY KEY,
    s_name TEXT NOT NULL,
    s_gender TEXT,
    s_mobile TEXT,
    s_email TEXT
)
''')

# Step 3: insert at least 5 records
students = [
    (1, 'aneela', 'F', '9876543210', 'ane@example.com'),
    (2, 'suppu', 'F', '9123456780', 'suppu@example.com'),
    (3, 'sreevani', 'F', '9988776655', 'sri@example.com'),
    (4, 'deepthi', 'F', '9012345678', 'deep@example.com'),
    (5, 'nikatha', 'F', '9898989898', 'nikhi@example.com')
]

cursor.executemany("INSERT INTO batch_53r VALUES (?, ?, ?, ?, ?)", students)
conn.commit()

# Step 4: display data
cursor.execute("SELECT * FROM batch_53r")
rows = cursor.fetchall()

print("Students in batch_53r:")
print("S.No | Name         | Gender | Mobile      | Email")
print("---------------------------------------------------------------")
for row in rows:
    print(f"{row[0]:<4} | {row[1]:<12} | {row[2]:<6} | {row[3]:<11} | {row[4]}")

conn.close()




# import sqlite3

# # Connect to database (it will create if not exists)
# with sqlite3.connect("10000coders.db") as conn:
#     cursor = conn.cursor()

#     # Create table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS batch_53r (
#             s_no INTEGER PRIMARY KEY,
#             s_name TEXT NOT NULL,
#             s_gender TEXT,
#             s_mobile TEXT,
#             s_email TEXT
#         )
#     ''')

#     # Insert records
#     students = [
#         (1, 'Swetha', 'F', '9876543210', 'swe@example.com'),
#         (2, 'Nikitha', 'F', '9123456780', 'nikitha@example.com'),
#         (3, 'Bhavitha', 'F', '9988776655', 'bhavi@example.com'),
#         (4, 'Deepthi', 'F', '9012345678', 'deep@example.com'),
#         (5, 'Harika', 'F', '9898989898', 'hari@example.com')
#     ]
#     cursor.executemany("INSERT OR IGNORE INTO batch_53r VALUES (?, ?, ?, ?, ?)", students)

#     # Fetch and display data
#     print("S.No | Name        | Gender | Mobile      | Email")
#     print("-" * 55)
#     for s_no, s_name, s_gender, s_mobile, s_email in cursor.execute("SELECT * FROM batch_53r"):
#         print(f"{s_no:<4} | {s_name:<11} | {s_gender:<6} | {s_mobile:<11} | {s_email}")