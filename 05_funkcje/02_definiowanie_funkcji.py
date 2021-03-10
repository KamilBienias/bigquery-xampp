# Etap9. Odcinek: Tworzenie wlasnych funkcji

# uruchamiac z terminala:
# python3 02_definiowanie_funkcji.py
import pymysql
import datetime
import pandas as pd


# moja funkcja
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

try:
    #database connection
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="",
                                 database="bigquery_functions")
    cursor = connection.cursor()
    print("Connection successful")

    # jedna zmienna (u niego functions to nazwa bazy danych)
    # Przyjmowanym parametrem jest x a typem paramertu INT64
    # Nie dziala bo:
    # (1064, "You have an error in your SQL syntax;
    # check the manual that corresponds to your MariaDB server version for
    # the right syntax to use near 'AS (x * 5)' at line 1")
    # create_function = """
    # CREATE FUNCTION bigquery_functions.multiply_by_5(x INT) AS (x * 5);
    # """
    # cursor.execute(create_function);

    # print()
    # retrive_query = "SELECT bigquery_functions.multiply_by_5(10) AS result;"
    # # wyswietla wiersz po wierszu
    # cursor.execute(retrive_query)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")
