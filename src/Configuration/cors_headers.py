from flask import request

allowed_origins = ['http://localhost:3000', 'http://localhost:3001']

def add_cors_headers(response):
    origin = request.headers.get('Origin')
    print("origin - Start")    
    print(origin)
    print("origin - Stop")
    if origin in allowed_origins:
        response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
