
from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
from Configuration.cors_headers import add_cors_headers

def display_single_user():
    if request.method == 'GET':
        user_id = request.args.get('id')
        connection = get_database_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM user WHERE id = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
        print(user_data)
        connection.close

        user_dict = {
        'id': user_data[0],
        'LastName': user_data[1],
        'FirstName': user_data[2],
        'UserName': user_data[3]
        }

        response = jsonify(user_dict)
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)
