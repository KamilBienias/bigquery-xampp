# Etap7. Odcinek: DML

"""
Data Manipulation Language
Umozliwia operacje takie jak UPDATE, INSERT, DELETE
"""

# uruchamiac z terminala:
# python3 01_DML.py
import pymysql

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
                                 database="bigquery_DML")
    cursor = connection.cursor()
    # some other statements  with the help of cursor
    print("Connection successful")

    # tworzenie tabeli produktow
    createTableSql = """CREATE OR REPLACE TABLE bigquery_DML.products(
    product_id INT NOT NULL,
    product_name VARCHAR(30),
    quantity INT,
    price FLOAT
    );"""

    cursor.execute(createTableSql)
    print("Table 'products' created")

    # tworzenie tabeli zamowien
    createTableSql = """CREATE OR REPLACE TABLE bigquery_DML.orders(
        order_id INT NOT NULL,
        product_id INT NOT NULL,
        quantity INT,
        price FLOAT
        );"""

    cursor.execute(createTableSql)
    print("Table 'orders' created")

    print("Wstawienie wartości do products na piechote")
    insert_query = "INSERT INTO products VALUES(%s, %s, %s, %s);"
    row_to_insert = [1, "book", 30, 19.99]
    cursor.execute(insert_query, row_to_insert)
    row_to_insert = [2, "car", 10, 19900.00]
    cursor.execute(insert_query, row_to_insert)
    row_to_insert = [3, "oven", 100, 199.99]
    cursor.execute(insert_query, row_to_insert)
    row_to_insert = [4, "tv", 15, 399.99]
    cursor.execute(insert_query, row_to_insert)

    print("Rows inserted to the table 'products'")

    print()
    show_table("bigquery_DML.products")

    print()
    print("Wstawienie pierwszej wartości do orders")
    select_product_price = "SELECT price FROM bigquery_DML.products WHERE product_id = 1"
    cursor.execute(select_product_price)
    rows = cursor.fetchall()
    for row in rows:
        print("Cena z zapytania:")
        print(row)
        selected_price = row
    insert_query = "INSERT INTO orders VALUES(%s, %s, %s, %s);"
    row_to_insert = [1, 1, 2, selected_price]
    cursor.execute(insert_query, row_to_insert)

    print()
    print("Wstawienie drugiej wartości do orders")
    select_product_price = "SELECT price FROM bigquery_DML.products WHERE product_id = 4"
    cursor.execute(select_product_price)
    rows = cursor.fetchall()
    for row in rows:
        print("Cena z zapytania:")
        print(row)
        selected_price = row
    insert_query = "INSERT INTO orders VALUES(%s, %s, %s, %s);"
    row_to_insert = [2, 4, 1, selected_price]
    cursor.execute(insert_query, row_to_insert)

    print()
    print("Wstawienie trzeciej wartości do orders")
    select_product_price = "SELECT price FROM bigquery_DML.products WHERE product_id = 2"
    cursor.execute(select_product_price)
    rows = cursor.fetchall()
    for row in rows:
        print("Cena z zapytania:")
        print(row)
        selected_price = row
    insert_query = "INSERT INTO orders VALUES(%s, %s, %s, %s);"
    row_to_insert = [3, 2, 2, selected_price]
    cursor.execute(insert_query, row_to_insert)

    print("Rows inserted to the table 'orders'")

    print()
    show_table("bigquery_DML.orders")

    print()
    print("Usuniecie zamowienia nr2")
    # w google cloud bylo bez FROM
    delete_order = "DELETE FROM bigquery_DML.orders WHERE order_id = 2;"
    cursor.execute(delete_order)
    print("Zamowienie nr2 usuniete")

    print()
    show_table("bigquery_DML.orders")

    print()
    print("Usuniecie zamowien w ktorych cena > 1000")
    select_products_ids = "SELECT order_id FROM bigquery_DML.orders WHERE price > 1000"
    cursor.execute(select_products_ids)
    rows = cursor.fetchall()
    for row in rows:
        print("Id z zapytania:")
        print(row[0])
        do_usuniecia = row[0]
        # w google cloud bylo bez FROM
        delete_order = "DELETE FROM bigquery_DML.orders WHERE order_id = " + str(do_usuniecia) + ";"
        cursor.execute(delete_order)
        print("Zamowienie o id = " + str(do_usuniecia) + " zostalo usuniete")

    print()
    show_table("bigquery_DML.orders")

    # aktualizacja ceny w tabeli products
    update_price = """
    UPDATE bigquery_DML.products
    SET price = 24.99
    WHERE product_id = 1;
    """
    cursor.execute(update_price)

    # aktualizacja ilosci w tabeli products
    update_quantity = """
        UPDATE bigquery_DML.products
        SET quantity = 99
        WHERE product_id = 3;
        """
    cursor.execute(update_quantity)

    print()
    show_table("bigquery_DML.products")

    print()
    #commiting the connection then closing it.
    connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()
    print("Connection closed")