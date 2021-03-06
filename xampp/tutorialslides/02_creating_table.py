# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 02_creating_table.py
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_data_types" )
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")

# Query for creating table
ArtistTableSql = """CREATE TABLE Artists(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  CHAR(20) NOT NULL,
TRACK CHAR(10))"""

cursor.execute(ArtistTableSql)

connection.close()
print("Connection closed")