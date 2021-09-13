import sqlite3

connection = sqlite3.connect("UserData.db")
cursor = connection.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

# cursor.execute("""
# INSERT INTO Users() VALUES(?,?)
# """)

# connection.commit()

print("Conectado ao Banco de Dados!")
