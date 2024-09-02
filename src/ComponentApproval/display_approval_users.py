
from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
from Configuration.cors_headers import add_cors_headers

def display_approval_users():
    if request.method == 'GET':
        connection = get_database_connection()
        cursor = connection.cursor()

        # Fetch all records from the 'user' table
        cursor.execute("SELECT id, LastName, FirstName, UserName FROM user")
        users = cursor.fetchall()
        users_json = []
        for user in users:
            user_dict = {
                'id': user[0],
                'LastName': user[1],
                'FirstName': user[2],
                'UserName': user[3]
            }

            users_json.append(user_dict)
        response = jsonify(users_json)
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)