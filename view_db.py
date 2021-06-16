# loading in modules
import sqlite3

# creating file path
dbfile = 'yellow_book.db'
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [a for a in cur.execute("""SELECT * FROM users """)]
# here is you table list
print(table_list)


x = cur.execute("""SELECT * FROM users """)
print (x)
# Be sure to close the connection
con.close()
