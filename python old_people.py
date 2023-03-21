import sqlite3
import datetime

# connect to the database
conn = sqlite3.connect('people.db')
c = conn.cursor()

query = "SELECT first_name, age FROM people WHERE age >= 50 LIMIT 20"

c.execute(query)

results = c.fetchall()

print("Old People:")

for name, age in results:
    print(f"{name} is {age} years old.")

conn.close()
