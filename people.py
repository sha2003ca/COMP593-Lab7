import sqlite3
from faker import Faker
import datetime
import random

# Connect to the database
conn = sqlite3.connect('people.db')
c = conn.cursor()

# Create the people table
c.execute('''CREATE TABLE people
             (id INTEGER PRIMARY KEY,
              first_name TEXT,
              last_name TEXT,
              age INTEGER,
              email TEXT,
              phone TEXT,
              created_at TEXT,
              updated_at TEXT)''')

# Insert 200 fake people into the people table
fake = Faker()
for i in range(200):
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(1, 100)
    email = fake.email()
    phone = fake.phone_number()
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO people (first_name, last_name, age, email, phone, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (first_name, last_name, age, email, phone, created_at, updated_at))

# Commit the changes and close the connection
conn.commit()
conn.close()