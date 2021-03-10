# Etap9. Odcinki: Funkcje COUNT, MIN, MAX, SUM, AVG.
# Funkcje: COUNTIF, ANY_VALUE, STRING_AGG

# uruchamiac z terminala:
# python3 03_funkcje_agregujace.py
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
#
    # tworzenie tabeli
    createTableSql = """CREATE OR REPLACE TABLE bigquery_functions.movies(
    id VARCHAR(5) NOT NULL,
    movie_name VARCHAR(30),
    rating FLOAT,
    duration FLOAT,
    is_polish BOOLEAN);
    """

    cursor.execute(createTableSql)
    print("Table created")
    insert_row = "INSERT INTO bigquery_functions.movies VALUES ('001', 'Batman', 4.5, 92.0, false);"
    cursor.execute(insert_row)
    insert_row = "INSERT INTO bigquery_functions.movies VALUES ('002', 'Spiderman', 4.75, 90.0, false);"
    cursor.execute(insert_row)
    insert_row = "INSERT INTO bigquery_functions.movies VALUES ('003', 'Django', 4.9, 160.0, false);"
    cursor.execute(insert_row)
    insert_row = "INSERT INTO bigquery_functions.movies VALUES ('004', 'Killer', 4.9, null, false);"
    cursor.execute(insert_row)
    insert_row = "INSERT INTO bigquery_functions.movies VALUES ('005', 'Gladiator', null, 155.0, false);"
    cursor.execute(insert_row)

    print("Rows inserted to the table")

    # cala tabela
    show_table("bigquery_functions.movies")

    print()
    print("Do funkcji agregujacych nulle sie nie licza")
    print("liczba wierszy, liczba rating, min rating, max rating")
    retrive_query = """
    SELECT 
        COUNT(*) AS total_count,
        COUNT(rating) AS non_null_rating_count,
        MIN(rating) AS min_rating,
        MAX(rating) AS max_rating,
        SUM(rating) AS sum_rating,
        AVG(rating) AS avg_rating
    FROM bigquery_functions.movies;"""
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    print()
    # ANY_VALUE zawraca losowa wartosc z kolumny
    # ANY_VALUE(movie_name) AS movie_name
    # oraz
    # COUNTIF(rating > 4.8) AS rating_count
    # rzucaja blad:
    # (1558, 'Column count of mysql.proc is wrong. Expected 21, found 20.
    # Created with MariaDB 100108, now running 100417.
    # Please use mysql_upgrade to fix this error')
    print("liczba wierszy, rating_count, liczba rating, min rating, max rating")
    retrive_query = """
        SELECT 
            COUNT(*) AS total_count,
            COUNT(rating) AS non_null_rating_count,      
            MIN(rating) AS min_rating,
            MAX(rating) AS max_rating,
            SUM(rating) AS sum_rating,
            AVG(rating) AS avg_rating
        FROM bigquery_functions.movies;"""
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # STRING_AGG polaczy stringi.
    # Domyslnie przecinkiem. Ale rzuca:
    # (1558, 'Column count of mysql.proc is wrong. Expected 21, found 20.
    # Created with MariaDB 100108, now running 100417.
    # Please use mysql_upgrade to fix this error')
    # retrive_query = """
    #         SELECT
    #             STRING_AGG(movie_name, '#' ORDER BY movie_name) AS movie_names
    #         FROM bigquery_functions.movies;
    #         """
    # # wyswietla wiersz po wierszu
    # cursor.execute(retrive_query)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    print()
    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")
