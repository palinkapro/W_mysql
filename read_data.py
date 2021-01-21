import db_connect as db

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_clients = "SELECT * FROM clients"
clients = execute_read_query(db.connection, select_clients)

for client in clients:
    print(client)