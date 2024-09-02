from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
import json  # Import the json module
from Configuration.cors_headers import add_cors_headers

def login_user_function():

    if request.method == 'POST':
        data = request.json
        userUserName = data.get('theUserName')
        userPassword = data.get('thePassword')

        mydb = get_database_connection()
        sql = "SELECT Password FROM user WHERE UserName = %s"
        mycursor = mydb.cursor()
        mycursor.execute(sql, [userUserName])
        result = mycursor.fetchone()

        if result is not None and len(result) > 0:
            if userPassword == result[0]:
                login_pwd_matching = 'true'
            else:
                login_pwd_matching = 'false'
        else:
            login_pwd_matching = 'false'
        response = jsonify({ 'login_pwd_matching': login_pwd_matching })
        print(response)
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)
