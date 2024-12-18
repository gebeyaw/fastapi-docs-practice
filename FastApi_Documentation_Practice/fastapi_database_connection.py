from fastapi import FastAPI
import time
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()

while True:
    try:
        # Connect to an existing database
        conn = psycopg2.connect(
            database="your_database_name",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432",
            cursor_factory=RealDictCursor
        )

        # Open a cursor to perform database operations
        cur = conn.cursor()
        print('database connected')
        break


    except Exception as error:
        print('connecting to database unsucessful')
        print('Error: ', error)
        time.sleep(2)


#creating an endpoint/path
@app.get("/users")
async def read_users():
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return {"users": users}


cur.close()
conn.close()