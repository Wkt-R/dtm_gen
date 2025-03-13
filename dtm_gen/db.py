import psycopg2

def connect_to_database(host, port, dbname, user, password):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        print("Database connection established successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        exit(1)

def get_data_from_table(conn, table_name, column_name, condition=None):
    cursor = conn.cursor()
    
    if condition:
        query = f"SELECT {column_name} FROM {table_name} WHERE {condition}"
    else:
        query = f"SELECT {column_name} FROM {table_name}"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception as e:
        print(f"Error querying database: {e}")
        cursor.close()
        return None