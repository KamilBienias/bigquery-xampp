# Etap5. Odcinek: Numeryczne typy danych

# uruchamiac z terminala:
# python3 01_numeryczne.py
import pymysql
import pandas as pd

"""
Numeryczne typy danych w BigQuery:

 - liczba całkowita: INT64:
 - storage: 8 bytes
 - zakres: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

 - numeryczny: NUMERIC: (dokładność do 9 liczby po przecinku)
    - storage: 16 bytes
    - zakres: -99999999999999999999999999999.999999999 to 99999999999999999999999999999.999999999

 - liczba zmiennoprzecinkowa: FLOAT64:
    - storage: 16 bytes
    - zakres: wartości dziesiętne podwójnej precyzji (przybliżone)
"""

try:
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery" )
    cursor = connection.cursor()
    # some other statements  with the help of cursor
    print("Connection successful")

    # Query for creating table
    createTableSql = """CREATE TABLE IF NOT EXISTS 01_numeric(
    var1 INT(20),
    var2 FLOAT,
    var3 FLOAT)"""
    cursor.execute(createTableSql)
    print("Table created")

    # usuwam wiersze, jesli juz wczesniej byly
    deleteSql = "DELETE FROM 01_numeric; "
    cursor.execute(deleteSql)
    print("Previous content deleted (if there was)")

    # sam wymyslilem jak wstawiac wiersze z csv do bazy
    df = pd.read_csv("/home/dell/PycharmProjects/bigquery-course/00_wygenerowanie_danych/numeric_types.csv")
    print("df =")
    print(df)
    print()
    print(df.info())
    print()

    # wstawianie df do tabeli
    insert_row_query = "INSERT INTO 01_numeric(var1, var2, var3) VALUES(%s, %s, %s);"
    for row_number in range(len(df.index)):
        # print(tuple(df.loc[row_number]))
        row_to_insert = list(df.loc[row_number])
        cursor.execute(insert_row_query, row_to_insert)
    print("Rows inserted to the table")

    print()
    print("Tabela w bazie =")
    # pokazuje nazwy kolumn w tabeli
    columns_names_query = "SHOW COLUMNS FROM 01_numeric;"
    cursor.execute(columns_names_query)
    rows = cursor.fetchall()
    for row in rows:
       print(row[0], end=" ")
    print()
    # zapytanie do wyswietlenia wszystkich wierszy i kolumn
    retrive_query = "SELECT * FROM 01_numeric;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
       print(row)

    print()
    print("Obok oryginalnych kolumn wyswietla po rzutowaniu int na float i odwrotnie")
    query = """ 
    SELECT
      var1,
      var2,
      var3,
      CAST(var1 AS FLOAT) AS var1_float,
      CAST(var2 AS INT) AS var2_int,
      CAST(var3 AS INT) AS var3_int
    FROM
      `01_numeric`; """
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