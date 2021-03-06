# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 05_update.py
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_data_types")
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")

# Suppose, you want to rename the name of the first artist
# from Towang to Tauwang.
# To update any attribute of any entity do the following:

updateSql = "UPDATE Artists SET NAME='Tauwang' WHERE ID='1' ;"
cursor.execute(updateSql)

#commiting the connection then closing it.
connection.commit()
connection.close()
print("Connection closed")