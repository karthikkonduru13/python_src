
import mysql.connector #type: ignore

def get_database_connection():
    return mysql.connector.connect(
        host="mysql_c1",
        user="root",
        password="rootpassword",
        database="Banking"
    )

#connection = get_database_connection()
#print(connection)

