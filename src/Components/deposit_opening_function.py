from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
import json  # Import the json module
from Configuration.cors_headers import add_cors_headers

def deposit_opening_function():
    if request.method == 'POST':
        data = request.json
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        depositAmt = data.get('depositAmt')
        tenor = data.get('tenor')
        depositType = data.get('depositType')
        mydb = get_database_connection()

        sql = "INSERT INTO deposit (firstName, lastName, depositamt, tenor, deposittype) VALUES (%s, %s, %s, %s, %s)"
        val = (firstName, lastName, depositAmt, tenor, depositType)

        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        response = jsonify({ 'deposit_status': "The Deposit opened successfully" })
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)