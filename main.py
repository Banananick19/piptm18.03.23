import sqlite3
from sqlite3 import Error



def sql_connection():
    try:

        con = sqlite3.connect(':memory:')

        print("Connection is established: Database is created in memory")
        return con
    except Error:

        print(Error)


def sql_table_employers(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()

def sql_insert_employer(con, entity):
    cursorObj = con.cursor()
    cursorObj.execute(
        '''INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)''',
        entity)

def sql_table_town(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE town(id integer PRIMARY KEY, name text)")
    con.commit()

    cursorObj.execute(
        "CREATE TABLE street(id integer PRIMARY KEY, name text, townId integer references town (id))")

    con.commit()

def sql_insert_town(con, entity):
    cursorObj = con.cursor()
    cursorObj.execute(
        '''INSERT INTO town(id, name) VALUES(?, ?)''',
        entity)
def sql_insert_street(con, entity):
    cursorObj = con.cursor()
    cursorObj.execute(
        '''INSERT INTO street(id, name, townId) VALUES(?, ?, ?)''',
        entity)

def print_streets(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM street')
    [print(row) for row in cursorObj.fetchall()]


def main():
    con = sql_connection()
    sql_table_town(con)
    sql_insert_town(con, (0, "Вологда"))
    sql_insert_street(con, (0, "Первомайская", 0))
    sql_insert_street(con, (1, "Дальная", 0))
    sql_insert_street(con, (2, "Архангельская", 0))
    sql_insert_street(con, (3, "Саммера", 0))
    sql_insert_street(con, (4, "Гоголя", 0))
    print_streets(con)


if __name__ == "__main__":
    main()