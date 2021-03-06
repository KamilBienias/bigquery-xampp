# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 04_select.py
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery" )
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")

print()
print("Tabela w bazie =")
# pokazuje nazwy kolumn w tabeli
columns_names_query = "SHOW COLUMNS FROM Artists;"
cursor.execute(columns_names_query)
rows = cursor.fetchall()
for row in rows:
   print(row[0], end=" ")
print()
# zapytanie do wyswietlenia wszystkich wierszy i kolumn
retrive_query = "SELECT * FROM Artists;"
# wyswietla wiersz po wierszu
cursor.execute(retrive_query)
rows = cursor.fetchall()
for row in rows:
   print(row)


#commiting the connection then closing it.
connection.commit()
connection.close()
print("Connection closed")