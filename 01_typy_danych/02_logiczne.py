# Etap5. Odcinek: Logiczne typy danych

# uruchamiac z terminala:
# python3 02_logiczne.py
import pymysql
import pandas as pd



try:
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery" )
    cursor = connection.cursor()
    # some other statements  with the help of cursor
    print("Connection successful")

    # Query for creating table
    createTableSql = """CREATE TABLE IF NOT EXISTS 02_logic(
    var1 INT,
    var2 BOOLEAN,
    var3 BOOLEAN,
    var4 BOOLEAN)"""
    cursor.execute(createTableSql)
    print("Table created")

    # usuwam wiersze, jesli juz wczesniej byly
    deleteSql = "DELETE FROM 02_logic; "
    cursor.execute(deleteSql)
    print("Previous content deleted (if there was)")

    # sam wymyslilem jak wstawiac wiersze z csv do bazy
    df = pd.read_csv("/home/dell/PycharmProjects/bigquery-course/00_wygenerowanie_danych/boolean_types.csv")
    print("df =")
    print(df)
    print()
    print(df.info())
    print()

    # zamieniam T na True i F na False bo byl blad przy zapisie do bazy
    df.loc[0, "var3"] = True
    df.loc[1, "var3"] = False
    df.loc[2, "var3"] = False
    df.loc[3, "var3"] = False

    print()
    print("df po zmianie var3 =")
    print(df)
    print()
    print(df.dtypes)
    print()

    # wstawianie df do tabeli
    insert_row_query = "INSERT INTO 02_logic(var1, var2, var3, var4) VALUES(%s, %s, %s, %s);"
    for row_number in range(len(df.index)):
        # print(list(df.loc[row_number]))

        row_to_insert = list(df.loc[row_number])
        # zamieniam kolumny var2, var3, var4 z boolean na int,
        # bo byl blad przy wstawianiu do tabeli
        row_to_insert[1] = int(row_to_insert[1])
        row_to_insert[2] = int(row_to_insert[2])
        row_to_insert[3] = int(row_to_insert[3])

        cursor.execute(insert_row_query, row_to_insert)
    print("Rows inserted to the table")

    print()
    print("Tabela w bazie =")
    # pokazuje nazwy kolumn w tabeli
    columns_names_query = "SHOW COLUMNS FROM 02_logic;"
    cursor.execute(columns_names_query)
    rows = cursor.fetchall()
    for row in rows:
       print(row[0], end=" ")
    print()
    # zapytanie do wyswietlenia wszystkich wierszy i kolumn
    retrive_query = "SELECT * FROM 02_logic;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
       print(row)

    # nid da sie rzutowac int na boolean
    # print()
    # print("Obok oryginalnych kolumn wyswietla po rzutowaniu int na boolean")
    # query = """
    # SELECT
    #   var1,
    #   var2,
    #   var3,
    #   var4,
    #   CAST(var1 AS BOOLEAN) AS var1_boolean,
    #   CAST(var2 AS BOOLEAN) AS var2_boolean,
    #   CAST(var3 AS BOOLEAN) AS var3_boolean,
    #   CAST(var4 AS BOOLEAN) AS var4_boolean
    # FROM
    #   `02_logic`; """
    # cursor.execute(query)
    # rows = cursor.fetchall()
    # for row in rows:
    #    print(row)

    print()
    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")