from flask import Flask, request, jsonify #type: ignore

from Configuration.db_connection import get_database_connection
from Configuration.cors_headers import add_cors_headers

def registration_function():
    if request.method == 'POST':
        data = request.json
        LastName = data.get('varLastName')
        FirstName = data.get('varFirstName')
        UserName = data.get('varUserName')
        Password = data.get('varPassword')

        sql = "INSERT INTO user (LastName, FirstName, UserName, Password) VALUES (%s, %s, %s, %s)"
        val = (LastName, FirstName, UserName, Password)

        mydb = get_database_connection()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        response = jsonify({ 'the_rows_inserted': str(mycursor.rowcount) })
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)