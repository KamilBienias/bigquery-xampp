# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 04_select.py
import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_data_types" )
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")

print("Moja funkcja")


def show_table(base_and_table_name):
   # pokazuje nazwy kolumn w tabeli
   print("Tabela " + base_and_table_name + " w bazie =")
   columns_names_query = "SHOW COLUMNS FROM " + base_and_table_name + ";"
   cursor.execute(columns_names_query)
   rows = cursor.fetchall()
   for row in rows:
      print(row[0], end=" ")
   print()
   retrive_query = "SELECT * FROM " + base_and_table_name + ";"
   # wyswietla wiersz po wierszu
   cursor.execute(retrive_query)
   rows = cursor.fetchall()
   for row in rows:
      print(row)

show_table("bigquery_data_types.Artists")

# print()
# print("Tabela w bazie =")
# # pokazuje nazwy kolumn w tabeli
# columns_names_query = "SHOW COLUMNS FROM Artists;"
# cursor.execute(columns_names_query)
# rows = cursor.fetchall()
# for row in rows:
#    print(row[0], end=" ")
# print()
# # zapytanie do wyswietlenia wszystkich wierszy i kolumn
# retrive_query = "SELECT * FROM Artists;"
# # wyswietla wiersz po wierszu
# cursor.execute(retrive_query)
# rows = cursor.fetchall()
# for row in rows:
#    print(row)


#commiting the connection then closing it.
connection.commit()
connection.close()
print("Connection closed")