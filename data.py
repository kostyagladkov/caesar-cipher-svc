import sqlite3
import caesar

conn = sqlite3.connect('cipher_database.db')

c = conn.cursor()

c.execute("""CREATE TABLE cipher(encode text, decode text)""")

#For test
#c.execute("INSERT INTO cipher VALUES ('abcd', 'bcde')")


x1 = caesar.encode("abcde", 1)

x2 = caesar.decode("bcdef", 1)

c.execute("INSERT INTO cipher VALUES (:encode, :decode)", {'encode': x1, 'decode': x2} )

conn.commit()



"""
----------------------
SHOW ALL TABLE CONTEXT
----------------------

c.execute('SELECT * FROM cipher')

rows = c.fetchall()

for row in rows:

    print(row)

"""



conn.close()