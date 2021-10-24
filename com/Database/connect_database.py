# https://chercher.tech/python/database-testing-selenium-python
# https://pynative.com/python-mysql-database-connection/
# importing the module
import mysql.connector
from mysql.connector import Error
from selenium import webdriver
# cerate a database connection
db = mysql.connector.connect("localhost","userName","Password","DB_Name")

# define a cursor object
cursor = db.cursor()
query = "select * from customers"
# drop table if exists
cursor.execute(query)

for col in cursor:
	driver.find_element_by_name("username").send_keys(col[0])
	driver.find_element_by_name("password").send_keys(col[1])
	driver.find_element_by_name("login").click
# Valdation
if driver.title == "Expected":
	assert True
else:
	assert False

res = cursor.fetchone() # or fetchall() method
for i in res:
	print(i)
# query
sql = "create table STUDENT (NAME CHAR(30) not null,
		CLASS char(5),
		AGE int,
		GENDER char(8),
		MARKS int"

# execute query
cursor.execute(sql)

# close object
cursor.close()

# close connection
db.close()
# validation
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
