
from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
from Configuration.cors_headers import add_cors_headers

def update_approval_user():
    if request.method == 'POST':    
        user_id = request.args.get('id')
        sql = "update user set status = 'Approved' where id=%s"
        val = (user_id,)

        mydb = get_database_connection()
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        response = jsonify({'message': mycursor.rowcount})
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)
