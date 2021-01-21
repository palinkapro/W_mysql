import db_connect as db

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_clients = """
INSERT INTO
  `clients` (`name`)
VALUES
  ('Name_1');
"""

execute_query(db.connection, create_clients)  