import sqlite3
import caesar



def db_connect():

	conn = sqlite3.connect('cipher_database.db')

	c = conn.cursor()

	#c.execute("""CREATE TABLE cipher(encode text, decode text)""")

	c.execute("INSERT INTO cipher VALUES (:encode, :decode)", {'encode': x1, 'decode': x2} )

	conn.commit()
	
	conn.close()


def db_setter(text, key):

	global x1

	global x2

	x1 = caesar.encode(text,key)

	x2 = caesar.decode(x1,key)



def db_getter(search):

	conn = sqlite3.connect('cipher_database.db')

	c = conn.cursor()

	find_e = search

	c.execute("SELECT * FROM cipher WHERE ENCODE = '{}'".format(find_e))
	print(c.fetchone())

	print("Done")
	#----------------------
	#SHOW ALL TABLE CONTEXT
	#----------------------
	#c.execute('SELECT * FROM cipher ')
	#rows = c.fetchall()
	#for row in rows:
	#	print(row)
	#conn.commit()

	conn.close()

db_setter()
db_connect()
db_getter()