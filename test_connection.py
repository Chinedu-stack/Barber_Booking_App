import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(
    host=os.environ["BARBER_DB_HOST"],
    port=int(os.environ["BARBER_DB_PORT"]),
    dbname=os.environ["BARBER_DB_NAME"],
    user=os.environ["BARBER_DB_USER"],
    password=os.environ["BARBER_DB_PASSWORD"],
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        print(cur.fetchone()[0])

print("Connection successful!")

