from flask import Flask, jsonify, request
from service import UserService, AreasService, EquipmentsService, CandidateService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def hw():
    return jsonify({'msg': 'Hello World'})

#------------User----------------
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

#------------Areas----------------

@app.route('/api/getAreaById', methods=['GET'])
def GetAreaById():
    return AreasService.GetAreaById(request)

@app.route('/api/getAreaByCode', methods=['GET'])
def GetAreaByCode():
    return AreasService.GetAreaByCode(request)

@app.route('/api/insertArea', methods=['POST'])
def InsertArea():
    return AreasService.InsertArea(request)

#------------Equipments----------------
@app.route('/api/getEquipmentById', methods=['GET'])
def GetEquipmentById():
    return EquipmentsService.GetEquipmentById(request)

@app.route('/api/getEquipmentByCode', methods=['GET'])
def GetEquipmentByCode():
    return EquipmentsService.GetEquipmentByCode(request)

@app.route('/api/insertEquipment', methods=['POST'])
def InsertEquipment():
    return EquipmentsService.InsertEquipment(request)

#-----------Candidate----------------

@app.route('/api/insertCandidate', methods=['POST'])
def InsertCandidate():
    return CandidateService.InsertCandidate(request)

@app.route('/api/getCandidates', methods=['GET'])
def GetCandidates():
    return CandidateService.GetCandidates()

@app.route('/api/getCandidateById', methods=['GET'])
def GetCandidateById():
    return CandidateService.GetCandidateById(request)
