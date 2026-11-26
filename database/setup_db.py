import os
import sys
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent
load_dotenv(BASE.parent / ".env")


def run_file(cursor, path):
    sql = path.read_text(encoding="utf-8")
    for statement in sql.split(";"):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)


conn = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
)
cursor = conn.cursor()

if "reset" in sys.argv:
    cursor.execute("DROP DATABASE IF EXISTS roomly")

run_file(cursor, BASE / "schema.sql")
run_file(cursor, BASE / "seed.sql")
conn.commit()

cursor.execute("SELECT COUNT(*) FROM rooms")
print("Done. Rooms in the database:", cursor.fetchone()[0])

cursor.close()
conn.close()