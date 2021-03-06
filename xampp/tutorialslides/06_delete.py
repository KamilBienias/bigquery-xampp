# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 06_delete.py
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_data_types" )
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")

deleteSql = "DELETE FROM Artists WHERE ID = '1'; "
cursor.execute(deleteSql)

#commiting the connection then closing it.
connection.commit()
connection.close()
print("Connection closed")