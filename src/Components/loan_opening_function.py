from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
import json  # Import the json module
from Configuration.cors_headers import add_cors_headers

def loan_opening_function():
    if request.method == 'POST':
        data = request.json
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        loanAmt = data.get('loanAmt')
        addressProof = data.get('addressProof')
        tenor = data.get('tenor')

        mydb = get_database_connection()

        sql = "INSERT INTO loan (firstName, lastName, loanAmount, addProof, tenor) VALUES (%s, %s, %s, %s, %s)"
        val = (firstName,lastName,loanAmt,addressProof,tenor)

        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        response = jsonify({'message': 'Function loan_opening_function'})
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)

