
from flask import Flask, request, jsonify #type: ignore
from Configuration.db_connection import get_database_connection
from Configuration.cors_headers import add_cors_headers
import os,json
#import pdb

def account_opening_function():
    if request.method == 'POST':
        json_data = request.form['data1']
        data = json.loads(json_data)
        print(data)
        varFirstName = data.get('firstName')
        varSecondName = data.get('lastName')
        varAddressProof = data.get('addressProof')
        varStreet = data.get('street')
        varCity = data.get('city')
        varAccountType = data.get('accountType')
        print("varAccountType1")
        print(varAccountType)
        print("varAccountType2")

    if 'image1' in request.files:
#        pdb.set_trace()
        pdf_file = request.files['image1']        
        pdf_file.save(os.path.join('uploads', pdf_file.filename))
        varImageFileName = pdf_file.filename
        splitFileName = os.path.splitext(varImageFileName)
        varImageFileType = splitFileName[1]

        mydb = get_database_connection()
        sql = "INSERT INTO account (firstName,secondName,addressProof,street,city,accounttype,add_proof_image_name,add_proof_image_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (varFirstName, varSecondName, varAddressProof, varStreet,varCity,varAccountType,varImageFileName,varImageFileType)

        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        response = jsonify({'message': 'Account successfully created'})
        return add_cors_headers(response)

    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        return add_cors_headers(response)
