"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime
from faker import Faker



# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')



def main():
    create_people_table()
    populate_people_table()



def create_people_table():
    """Creates the people table in the database"""
    conn = sqlite3.connect('social_network.db')
    c = conn.cursor()
    

    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
        (
            id          INTEGER PRIMARY KEY,
            name        TEXT NOT NULL,
            email       TEXT NOT NULL,
            address     TEXT NOT NULL,
            city        TEXT NOT NULL,
            province    TEXT NOT NULL,
            bio         TEXT,
            age         INTEGER,
            created_at  DATETIME NOT NULL,
            updated_at  DATETIME NOT NULL
        );
    """
    c.execute(create_ppl_tbl_query)
    conn.commit()
    conn.close()
    #TODOCreate function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    return



def populate_people_table():
    """Populates the people table with 200 fake people"""
    conn = sqlite3.connect('social_network.db')
    c = conn.cursor()
    
    fake = Faker("en_CA")

    for _ in range(200):
        name = fake.name()
        email = fake.email()
        address = fake.street_address()
        city = fake.city()
        province = fake.administrative_unit()
        bio = fake.sentence()
        age = fake.random_int(min=1, max=100)
        created_at = datetime.now()
        updated_at = datetime.now()

        add_person_query = """
            INSERT INTO people
            (
                name,
                email,
                address,
                city,
                province,
                bio,
                age,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        c.execute(add_person_query, (name, email, address, city, province, bio, age, created_at, updated_at))
    conn.commit()
    conn.close()
    
    # TODOCreate function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    return

if __name__ == '__main__':
   main()