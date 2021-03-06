# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 01_connection.py
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_data_types" )
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")
connection.close()
print("Connection closed")