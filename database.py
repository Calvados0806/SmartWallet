"this module contains functions for request to database"

import mysql.connector
from mysql.connector import errorcode
import config as cnf

conn = mysql.connector.connect(
	user=cnf.USER,
	password=cnf.PASSWORD
)
cursor = conn.cursor()

def create_database(cursor):
	"creates database"
	try:
		cursor.execute(
			"CREATE DATABASE {0} DEFAULT CHARACTER SET 'utf8'".format(cnf.DB_NAME)
		)
	except mysql.connector.Error as err:
		raise

def get_balance(cursor):
	"returns balance from database"
	cursor.execute(
		"SELECT balance FROM cash"
	)
	l = list(cursor)
	if l:
		return l[0][0]
	return None

def supply(cursor, n):
	"changes value in table `cash`"
	last = get_balance(cursor)
	if not last:
		cursor.execute(
			"INSERT INTO cash VALUES ({0})".format(n)
		)
		conn.commit()
	else:
		cursor.execute(
			"UPDATE cash SET balance = {0}".format(n + last)
		)
		conn.commit()

def get_history(cursor, n=None):
	"returns list of info about purchases"
	cursor.execute(
		"SELECT * FROM history"
	)
	result = list(cursor)
	if n and n < len(result):
		return result[-n:]
	return result

def discard(cursor, n, message):
	"inserts values in table history"
	cursor.execute(
		"INSERT INTO history VALUES (NULL, %(n)s, %(message)s)", {"n": n, "message": message}
	)
	conn.commit()

try:
	#set db name and create tables
	create_database(cursor)
	conn.database = cnf.DB_NAME
	for cmd in cnf.TABLES.values():
		cursor.execute(cmd)
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_DB_CREATE_EXISTS or\
		err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
		#if db or tables are already exist ignore that
		pass
	else:
		print(err)
		exit(1)
conn = mysql.connector.connect(
	user=cnf.USER,
	password=cnf.PASSWORD,
	host=cnf.HOST,
	database=cnf.DB_NAME
)
cursor = conn.cursor(buffered=True)