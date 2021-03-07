# https://www.dataquest.io/blog/sql-insert-tutorial/

# uruchamiac z terminala:
# python3 01_insert_df_moje_i_sqlalchemy.py
import pymysql
import datetime
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
                                 database="bigquery_data_types")
    cursor = connection.cursor()
    print("Connection successful")

    # tworzenie tabeli
    createTableSql = """CREATE OR REPLACE TABLE bigquery_data_types.wszystkie_typy(
    id INT NOT NULL,
    name VARCHAR(30),
    has_married BOOLEAN,
    date_of_birth DATE,
    insert_timestamp TIMESTAMP
    );"""

    cursor.execute(createTableSql)
    print("Table created")

    print("Wstawienie wartości na piechote (bez df)")
    insert_query = "INSERT INTO bigquery_data_types.wszystkie_typy VALUES(%s, %s, %s, %s, %s);"
    row_to_insert = [1, "Mark", True, datetime.date(1990, 10, 1), datetime.datetime.now()]
    cursor.execute(insert_query, row_to_insert)
    row_to_insert = [2, "Tom", False, datetime.date(1992, 2, 13), datetime.datetime.now()]
    cursor.execute(insert_query, row_to_insert)
    row_to_insert = [3, "John", True, datetime.date(1989, 5, 24), datetime.datetime.now()]
    cursor.execute(insert_query, row_to_insert)

    print("Rows inserted to the table")

    show_table("bigquery_data_types.wszystkie_typy")

    print("-------------------------------------------------------")
    print("Wstawianie wartosci z df moim sposobem.")
    print("Kolumny w df moga sie inaczej nazywac niz kolumny w tabeli (zaleta).")
    print("MUsze wiedziec ile jest kolumn (wada)")
    df = pd.DataFrame(data={
        "id_df_column": [4, 5, 6],
        "name_df_column": ["Jurek", "Darek", "Jarek"],
        "has_married_df_column": [True, True, False],
        "date_of_birth_df_column": [datetime.date(1967, 3, 25), datetime.date(2003, 11, 15), datetime.date(2001, 1, 30)],
        "insert_timestamp_df_column": [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
    })

    print("df =")
    print(df)
    print(df.info())

    print("Zamieniam boolean na int bo byl blad")
    df["has_married_df_column"] = df["has_married_df_column"].astype("int8")

    print("df =")
    print(df)
    print(df.info())

    print()
    # wstawianie df do tabeli
    insert_row_query = """
    INSERT INTO bigquery_data_types.wszystkie_typy(id, 
                                                   name, 
                                                   has_married, 
                                                   date_of_birth, 
                                                   insert_timestamp) 
    VALUES(%s, %s, %s, %s, %s);
    """
    for row_number in range(len(df.index)):
        row_to_insert = list(df.loc[row_number])
        cursor.execute(insert_row_query, row_to_insert)
    print("Rows inserted to the table")

    show_table("bigquery_data_types.wszystkie_typy")

    print("-------------------------------------------------------")
    print("Wstawianie wartosci z df sposobem z dataquest (bez sqlalchemy)")
    print("Nie musze sie martwic iloscia kolumn (zaleta)")
    print("Nie trzeba zamieniac boolean na int (zaleta)")
    df = pd.DataFrame(data={
        "id": [7, 8, 9],
        "name": ["Adam", "Bartek", "Czarek"],
        "has_married": [False, True, True],
        "date_of_birth": [datetime.date(1967, 3, 25), datetime.date(2003, 11, 15), datetime.date(2001, 1, 30)],
        "insert_timestamp": [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
    })

    print()
    # creating column list for insertion
    cols_from_df = ",".join([str(i) for i in df.columns.tolist()])
    print("cols_from_df =")
    print(cols_from_df)

    # sam pobieram kolumny z tabeli
    columns_names_query = "SHOW COLUMNS FROM bigquery_data_types.wszystkie_typy;"
    cursor.execute(columns_names_query)
    rows = cursor.fetchall()
    cols_from_table = []
    for row in rows:
        # print(row[0], end=" ")
        cols_from_table.append(row[0])
    cols_from_table = ",".join([str(i) for i in cols_from_table])
    print("cols_from_table =")
    print(cols_from_table)

    # Insert DataFrame records one by one.
    for i, row in df.iterrows():
        # mozna brac kolumny z df lub kolumny z tabeli, czyli moge tez cols_form_df
        sql = "INSERT INTO bigquery_data_types.wszystkie_typy (" + cols_from_table + ") VALUES (" + "%s," * (len(row) - 1) + "%s)"
        cursor.execute(sql, tuple(row))

    print()
    show_table("bigquery_data_types.wszystkie_typy")

    print("-------------------------------------------------------")
    print("Wstawianie wartosci z df uzywajac sqlalchemy (sposob z dataquest)")
    print("Niestety u mnie nie dziala bo Background on this error at: http://sqlalche.me/e/13/e3q8")
    # df = pd.DataFrame(data={
    #     "id": [10, 11, 12],
    #     "name": ["Irek", "Maurycy", "Daniel"],
    #     "has_married": [False, False, True],
    #     "date_of_birth": [datetime.date(1967, 3, 25), datetime.date(2003, 11, 15), datetime.date(2001, 1, 30)],
    #     "insert_timestamp": [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
    # })
    #
    # # import the module
    # from sqlalchemy import create_engine
    #
    # # create sqlalchemy engine
    # engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
    #                        .format(user="root",
    #                                pw="",
    #                                db="bigquery_data_types"))
    #
    # # Insert whole DataFrame into MySQL
    # df.to_sql('wszystkie_typy', con=engine, if_exists='append', chunksize=1000)
    #
    # show_table("bigquery_data_types.wszystkie_typy")

    print()
    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")
