from Components.login_user_function import login_user_function
from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
import json  # Import the json module
from Configuration.cors_headers import add_cors_headers
import pdb

def login_user_function_debug():

        data = {
"theUserName": "user",
"thePassword": "password123"
}
        userUserName = data.get('theUserName')
        userPassword = data.get('thePassword')

#        pdb.set_trace()

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
#        response = jsonify({ 'login_pwd_matching': login_pwd_matching })
        response = login_pwd_matching

        return response



kk = login_user_function_debug()
print(kk)
