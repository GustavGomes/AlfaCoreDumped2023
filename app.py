from flask import Flask, jsonify, request
from service import UserService
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['GET'])
def hw():
    return jsonify({'msg': 'Hello World'})

@app.route('/api/login', methods=['POST'])
def userLogin():
    print("Login request received")
    return UserService.Login(request)

@app.route('/api/insertUser', methods=['POST'])
def insertUser():
    return UserService.InsertUser(request)

@app.route('/api/updateUser', methods=['POST'])
def UpdateUser():
    return UserService.UpdateUser(request)

@app.route('/api/deleteUser', methods=['POST'])
def DeleteUser():
    return UserService.DeleteUser(request)