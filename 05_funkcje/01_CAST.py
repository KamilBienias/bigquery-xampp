# Etap8. Odcinek: Funkcja CAST

# uruchamiac z terminala:
# python3 01_CAST.py
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
    df = pd.read_csv("/home/dell/PycharmProjects/bigquery-course/00_wygenerowanie_danych/people.csv",)
    print("df.index =")
    print(df.index)
    print()
    print("df.info() =")
    print(df.info())

    #database connection
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="",
                                 database="bigquery_functions")
    cursor = connection.cursor()
    print("Connection successful")
#
    # tworzenie tabeli
    createTableSql = """CREATE OR REPLACE TABLE bigquery_functions.people(
    age INT,
    name VARCHAR(30),
    has_married BOOLEAN,
    has_house INT,
    height FLOAT
    );"""

    cursor.execute(createTableSql)
    print("Table created")

    print()
    # creating column list for insertion
    cols_from_df = ",".join([str(i) for i in df.columns.tolist()])
    print("cols_from_df =")
    print(cols_from_df)

    # Insert DataFrame records one by one.
    for i, row in df.iterrows():
        # mozna brac kolumny z df lub kolumny z tabeli, czyli moge tez cols_form_df
        sql = "INSERT INTO bigquery_functions.people (" + cols_from_df + ") VALUES (" + "%s," * (
                    len(row) - 1) + "%s)"
        cursor.execute(sql, tuple(row))

    print("Rows inserted to the table")

    # cala tabela
    show_table("bigquery_functions.people")

    # skladnia przy rzutowaniu
    # CAST(expression AS typename)

    print()
    print("Ostatnia kolumna to age zrzutowany na float")
    retrive_query = "SELECT *, CAST(age AS FLOAT) AS age_float FROM bigquery_functions.people;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print()
    print("Ostatnia kolumna to age zrzutowany na string")
    retrive_query = "SELECT *, CAST(age AS VARCHAR(30)) AS age_string FROM bigquery_functions.people;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print()
    print("Ostatnia kolumna to age zrzutowany na string oraz dodany 'years old'")
    retrive_query = "SELECT *, CONCAT(CAST(age AS VARCHAR(30)), ' years old') AS age_string FROM bigquery_functions.people;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print()
    print("Bezpieczne castowanie")
    # to nie dzialalo (nawet SAFE_CAST):
    # CAST(2 AS BOOLEAN) AS is_purchased
    # Natomiast SAFE_CAST("a" AS DATE) AS date;
    # wyrzucilo blad zamiast null:
    # (1584, "Incorrect parameters in the call to stored function 'SAFE_CAST'")

    retrive_query = """
    SELECT 
        CAST('001' AS INT) AS id;
    """
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)



    print()
    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")
