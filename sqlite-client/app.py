import sqlite3
import os

def create_connection(db_file):
    """ Create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        if not os.path.exists(os.path.dirname(db_file)):
            os.makedirs(os.path.dirname(db_file))
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file} SQLite version {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """ Create a table in the SQLite database """
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer
                            );"""
        c = conn.cursor()
        c.execute(sql_create_table)
    except sqlite3.Error as e:
        print(e)

def insert_task(conn, task):
    """ Insert a new task into the tasks table """
    sql_insert_task = '''INSERT INTO tasks(name, priority)
                         VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql_insert_task, task)
    conn.commit()
    return cur.lastrowid

def main():
    database = "/app/sqlite-client/tasks.db"

    # Create a database connection
    conn = create_connection(database)
    if conn is not None:
        # Create tasks table
        create_table(conn)

        # Insert a new task
        task = ('Sample Task', 1)
        task_id = insert_task(conn, task)
        print(f"Task created with id {task_id}")

        # Close the connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()