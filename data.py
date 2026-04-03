import pymysql
import os

# ---------------- CONFIG ----------------
FILE_PATH = r"C:\Users\RajaReddyKumarBalipo\Documents\Talend_to_Pyspark_jobs\app\agents\member_data_full_100000.csv"   # 👈 update this
TABLE_NAME = "member_data_cc_a"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "mysql",
    "database": "test",
    "allow_local_infile": True
}

# ---------------- CONNECT ----------------
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="test",
    local_infile=True
)

cursor = conn.cursor()

file_path = os.path.abspath(FILE_PATH).replace("\\", "/")

# ---------------- LOAD DATA ----------------
load_sql = f"""
LOAD DATA LOCAL INFILE '{file_path}'
INTO TABLE {TABLE_NAME}
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\\n'
IGNORE 1 ROWS;
"""

print("🚀 Loading CSV into MySQL...")

cursor.execute(load_sql)
conn.commit()

# ---------------- VERIFY ----------------
cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
count = cursor.fetchone()[0]

print(f"🎯 Data Loaded Successfully! Total rows: {count}")

# ---------------- CLOSE ----------------
cursor.close()
conn.close()