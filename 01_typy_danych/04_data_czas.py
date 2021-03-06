# Etap5. Odcinek: Data i czas

# uruchamiac z terminala:
# python3 04_data_czas.py
import pymysql
import pandas as pd

"""
data w BigQuery:

 - typ daty: DATE:
    - data kalendarzowa, np. 2019-01-01 (niezależnie od strefy czasowej)

 - typ daty: DATETIME:
    - reprezentuje rok, miesiąc, dzień, godzinę, minutę, sekundę i części ułakmowe sekundy. np. 2019-01-01 01:00:00 (konkretny punkt w czasie)

czas w BigQuery:

 - typ casu: TIME:
    - reprezentuje czas, niezależenie od daty, np. 00:04:45

 - typ czasu: TIMESTAMP:
    - reprezentuje punkt w czasie z mikrosekundową precyzją
"""

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
                                 database="bigquery_data_types")
    cursor = connection.cursor()
    # some other statements  with the help of cursor
    print("Connection successful")

    # Query for creating table
    createTableSql = """CREATE TABLE IF NOT EXISTS 04_date_time(
     var1 TIMESTAMP,
     var2 TIMESTAMP,
     var3 TIMESTAMP,
     var4 TIMESTAMP,
     var5 DATE,
     var6 TIME)"""
    cursor.execute(createTableSql)
    print("Table created")

    # usuwam wiersze, jesli juz wczesniej byly
    deleteSql = "DELETE FROM 04_date_time; "
    cursor.execute(deleteSql)
    print("Previous content deleted (if there was)")

    # sam wymyslilem jak wstawiac wiersze z csv do bazy
    # Zamieniam var1 z float na object
    df = pd.read_csv("/home/dell/PycharmProjects/bigquery-course/00_wygenerowanie_danych/date_time_types.csv")
    print("df =")
    print(df)
    print()
    print(df.info())

    # https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587
    df["var1"] = pd.to_datetime(df["var1"], format="%Y-%m-%d %H:%M:%S")
    df["var2"] = pd.to_datetime(df["var2"], format="%Y-%m-%d %H:%M:%S")
    df["var3"] = pd.to_datetime(df["var3"], format="%Y-%m-%d %H:%M:%S")
    df["var4"] = pd.to_datetime(df["var4"], format="%Y-%m-%d %H:%M:%S")
    df["var5"] = pd.to_datetime(df["var5"], format="%d-%m-%Y")
    df["var6"] = pd.to_datetime(df["var6"], format="%H:%M:%S")
    print("Po zamianie na daty df =")
    print(df)
    print()
    print(df.info())

    # moje wstawianie df do tabeli
    # (wtedy trzeba rzutowac object na datetime i boolean na int)
    insert_row_query = "INSERT INTO bigquery_data_types.04_date_time(var1, var2, var3, var4, var5, var6) VALUES(%s, %s, %s, %s, %s, %s);"
    for row_number in range(len(df.index)):
        row_to_insert = list(df.loc[row_number])
        cursor.execute(insert_row_query, row_to_insert)
    print("Rows inserted to the table")

    print()
    show_table("bigquery_data_types.04_date_time")

    # print()
    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")