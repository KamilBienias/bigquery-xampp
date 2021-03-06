# Etap6. Odcinek: Tworzenie tabel przy pomocy SQL cz. 1

# uruchamiac z terminala:
# python3 01_tworzenie_tabel.py
import pymysql
import pandas as pd

"""
 DDL - Data Definition Language - pozwala tworzyć i modfikować zasoby przy pomocy standardowego
języka SQL, np:
 - tworzenie tabel, widoków, funkcji zdefiniowanych przez użytkownika
 - zmiana tabel
 - usuwanie tabel i widoków

Tworzenie tabeli - SYNTAX

{CREATE TABLE | CREATE TABLE IF NOT EXISTS | CREATE OR REPLACE TABLE}
table_name
[(
  column_name column_schema[, ...]
)]
[PARTITION BY partition_expression]
[CLUSTER BY clustering_column_list]
[OPTIONS(table_option_list)]
[AS query_statement]
"""

try:
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_DDL" )
    cursor = connection.cursor()
    # some other statements  with the help of cursor
    print("Connection successful")

    # tworzenie tabeli
    createTableSql = """CREATE OR REPLACE TABLE bigquery_DDL.01_table(
    id VARCHAR(5),
    age INT,
    name VARCHAR(30));"""
    cursor.execute(createTableSql)
    print("Table created")

    # Wstawienie wartości
    insert_query = "INSERT INTO bigquery_DDL.01_table VALUES('001', 25, 'Mark');"
    cursor.execute(insert_query)
    insert_query = "INSERT INTO bigquery_DDL.01_table VALUES('002', 26, 'John');"
    cursor.execute(insert_query)
    insert_query = "INSERT INTO bigquery_DDL.01_table VALUES('003', 27, 'Frank');"
    cursor.execute(insert_query)
    insert_query = "INSERT INTO bigquery_DDL.01_table VALUES('004', 20, 'Mary');"
    cursor.execute(insert_query)

    print("Rows inserted to the table")

    # Zapytanie
    # pokazuje nazwy kolumn w tabeli
    print()
    print("Tabela w bazie =")
    columns_names_query = "SHOW COLUMNS FROM bigquery_DDL.01_table;"
    cursor.execute(columns_names_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], end=" ")
    print()
    retrive_query = "SELECT * FROM bigquery_DDL.01_table;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
       print(row)

    # Usuwanie tabeli
    # drop_table = "DROP TABLE IF EXISTS bigquery_DDL.01_table;"
    # cursor.execute(drop_table)
    # print("Table dropped")

    print()
    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")