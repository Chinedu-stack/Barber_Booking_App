import psycopg

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password=input("Enter your PostgreSQL password: "),
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        print(cur.fetchone()[0])

print("Connection successful!")