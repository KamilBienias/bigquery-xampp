# Etap6. Odcinek: Tabele tymczasowa

# uruchamiac z terminala:
# python3 03_tabela_tymczasowa.py
import pymysql
import datetime


try:
    #database connection
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 passwd="",
                                 database="bigquery_DDL")
    cursor = connection.cursor()
    # some other statements  with the help of cursor
    print("Connection successful")

    # tworzenie tabeli tymczasowej, nie bedzie w bazie
    # W bazie google jest TEMP
    createTableSql = """CREATE TEMPORARY TABLE temp_table(
    id VARCHAR(5),
    age INT,
    name VARCHAR(30)
    );"""

    cursor.execute(createTableSql)
    print("Table created")

    # Wstawienie wartości
    insert_query = "INSERT INTO temp_table VALUES(%s, %s, %s);"
    row_to_insert = ["001", 23, "Mark"]
    cursor.execute(insert_query, row_to_insert)
    row_to_insert = ["002", 34, "Kamil"]
    cursor.execute(insert_query, row_to_insert)
    row_to_insert = ["003", 38, "Michal"]
    cursor.execute(insert_query, row_to_insert)

    print("Rows inserted to the table")

    # pokazuje nazwy kolumn w tabeli
    # print()
    # print("Tabela w bazie =")
    # columns_names_query = "SHOW COLUMNS FROM temp_table;"
    # cursor.execute(columns_names_query)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row[0], end=" ")
    # print()

    print("Srednia wieku")
    retrive_query = "SELECT AVG(age) FROM temp_table;"
    # wyswietla wiersz po wierszu
    cursor.execute(retrive_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Usuwanie tabeli
    # drop_table = "DROP TABLE IF EXISTS bigquery_DDL.02_table;"
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