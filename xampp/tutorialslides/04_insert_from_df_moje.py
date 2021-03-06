# https://tutorialslides.com/how-to-connect-and-create-database-on-mysql-phpmyadmin-using-python/

# uruchamiac z terminala:
# python3 03_insert.py
import pymysql
import pandas as pd

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="bigquery_data_types" )
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Connection successful")

# # queries for inserting values
# insert1 = "INSERT INTO Artists(NAME, TRACK) VALUES(%s, %s);"
# insert2 = "INSERT INTO Artists(NAME, TRACK) VALUES(%s, %s);"
#
# #executing the quires
# cursor.execute(insert1, ("Kamil", "B"))
# cursor.execute(insert2, ("James", "Bond"))

# sam wymyslilem jak wstawiac wiersze z df do bazy
df = pd.DataFrame(data={
    "name": ["Robert", "Grzegorz"],
    "track": ["track R", "track G"]
})
print(df)
print()
print(df.info())
print()

insert_row_query = "INSERT INTO Artists(NAME, TRACK) VALUES(%s, %s);"

for row_number in range(len(df.index)):
    # print(tuple(df.loc[row_number]))
    row_to_insert = list(df.loc[row_number])
    cursor.execute(insert_row_query, row_to_insert)

#commiting the connection then closing it.
connection.commit()
connection.close()
print("Connection closed")