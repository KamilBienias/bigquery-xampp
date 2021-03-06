# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 07_drop_table.py
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery" )
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")

dropSql = "DROP TABLE IF EXISTS Artists;"
cursor.execute(dropSql)

#commiting the connection then closing it.
connection.commit()
connection.close()
print("Connection closed")