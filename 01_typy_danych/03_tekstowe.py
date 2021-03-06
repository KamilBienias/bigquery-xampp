# Etap5. Odcinek: Tekstowe typy danych

# uruchamiac z terminala:
# python3 03_tekstow.py
import pymysql
import pandas as pd

"""
 Tekstowy typ danych w BigQuery:
  - typ tesktowy: STRING:
  - łańcuch znaków o dowolnej długości, domyślne kodowanie UTF-8
"""

try:
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_data_types" )
    cursor = connection.cursor()
    # some other statements  with the help of cursor
    print("Connection successful")

    # Query for creating table
    createTableSql = """CREATE TABLE IF NOT EXISTS 03_text(
    var1 VARCHAR(30),
    var2 VARCHAR(30),
    var3 VARCHAR(30))"""
    cursor.execute(createTableSql)
    print("Table created")

    # usuwam wiersze, jesli juz wczesniej byly
    deleteSql = "DELETE FROM 03_text; "
    cursor.execute(deleteSql)
    print("Previous content deleted (if there was)")

    # sam wymyslilem jak wstawiac wiersze z csv do bazy
    # Zamieniam var1 z float na object
    df = pd.read_csv("/home/dell/PycharmProjects/bigquery-course/00_wygenerowanie_danych/string_types.csv",
                     dtype={'var1': 'object'})
    print("df =")
    print(df)
    print()
    print(df.info())

    # wstawianie df do tabeli
    insert_row_query = "INSERT INTO 03_text(var1, var2, var3) VALUES(%s, %s, %s);"
    for row_number in range(len(df.index)):
        # print(list(df.loc[row_number]))
        row_to_insert = list(df.loc[row_number])
        cursor.execute(insert_row_query, row_to_insert)
    print("Rows inserted to the table")

    print()
    print("Tabela w bazie =")
    # pokazuje nazwy kolumn w tabeli
    columns_names_query = "SHOW COLUMNS FROM 03_text;"
    cursor.execute(columns_names_query)
    rows = cursor.fetchall()
    for row in rows:
       print(row[0], end=" ")
    print()
    # zapytanie do wyswietlenia wszystkich wierszy i kolumn
    retrive_query = "SELECT * FROM 03_text;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
       print(row)

    print()
    print("Obok oryginalnych kolumn wyswietla po rzutowaniu var1 string na int i float")
    query = """
    SELECT
      var1,
      CAST(var1 AS INT) AS var1_int,
      CAST(var1 AS FLOAT) AS var1_float,
      var2,
      var3
    FROM
      `03_text`; """
    cursor.execute(query)
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