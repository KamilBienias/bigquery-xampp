# Etap8. Odcinek: Operatory arytmetyczne, porownania oraz logiczne

# uruchamiac z terminala:
# python3 05_operatory_stats_google.py
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

def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

try:
    df = fetch_financial_data('GOOGL')
    print("Stary index:")
    print(df.index)
    # kolumna Date byla indeksem, wiec trzeba zrobic zeby ona byla kolumna
    # bo inaczej nie jest zapisywana do bazy
    df = df.reset_index()
    print()
    print("Nowy index:")
    print(df.index)
    # nie trzeba zapisywac df do csv
    # df.to_csv('google.csv')
    print()
    print("df.info() =")
    print(df.info())

    #database connection
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="",
                                 database="bigquery_DQL")
    cursor = connection.cursor()
    print("Connection successful")
#
    # tworzenie tabeli
    createTableSql = """CREATE OR REPLACE TABLE bigquery_DQL.google(
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Volume INT
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
        sql = "INSERT INTO bigquery_DQL.google (" + cols_from_df + ") VALUES (" + "%s," * (
                    len(row) - 1) + "%s)"
        cursor.execute(sql, tuple(row))

    print("Rows inserted to the table")

    # za dluga zeby cala tabele pokazywac
    # show_table("bigquery_DQL.google")

    # pokazuje nazwy kolumn w tabeli
    print("Statystyki ceny zamkniecie w grupowaniu na lata i miesiace")
    print("year, month, suma,   min,   max,   srednia")
    retrive_query = """
    SELECT
        EXTRACT(YEAR FROM Date) AS year,
        EXTRACT(MONTH FROM Date) AS month,
        ROUND(SUM(Close), 2) AS suma_cen_zamkniecia,
        MIN(Close) AS minimalna_cena_zamkniecia,
        MAX(Close) AS maksymalna_cena_zamkniecia,
        ROUND(AVG(Close), 2) AS srednia_cena_zamkniecia
    FROM bigquery_DQL.google 
    GROUP BY
        year, month
    ORDER BY
        year, month;
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
