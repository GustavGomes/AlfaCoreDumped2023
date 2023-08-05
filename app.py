# Autores: Fernanda Mendes, Gustavo Gomes, Pedro Pampolini
# Sistema desenvolvido durante o Hackathon da Alfa Engenharia em 2023 
# O sistema segue o modelo de Service-DAO-Model:
# Model contém os modelos de dados representador no banco de dados
# DAO contém as funções de acesso ao banco de dados, com as queries necessárias
# Service contém as funções que são chamadas pelas rotas, e que chamam as funções do DAO,
# Service realiza algum tratamento prévio, como recuperar elementos do request

from flask import Flask, jsonify, request
from service import UserService, AreasService, EquipmentsService, CandidateService, ReportService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Criação das possiveis rotas do código
@app.route('/api', methods=['GET'])
def hw():
    return jsonify({'msg': 'Hello World'})


#------------ Rotas User ----------------
@app.route('/api/login', methods=['POST'])
def userLogin():
    print("Login request received")
    return UserService.Login(request)

# Rota que insere o usuário no banco de dados, apenas para testes
@app.route('/api/insertUser', methods=['POST'])
def insertUser():
    return UserService.InsertUser(request)

# Rota que atualiza o usuario no banco de dados, não utilizada no sistema no geral
@app.route('/api/updateUser', methods=['POST'])
def UpdateUser():
    return UserService.UpdateUser(request)

# Rota que atualiza o usuario no banco de dados, não utilizada no sistema no geral
@app.route('/api/deleteUser', methods=['POST'])
def DeleteUser():
    return UserService.DeleteUser(request)

#------------Areas----------------
@app.route('/api/getAreaById', methods=['GET'])
def GetAreaById():
    print("GetAreaById request received")
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
    print("GetCandidates request received")
    return CandidateService.GetCandidates()

@app.route('/api/getCandidateById', methods=['GET'])
def GetCandidateById():
    return CandidateService.GetCandidateById(request)


#-----------Reports----------------
@app.route('/api/getReportById', methods=['GET'])
def GetReportById():
    return ReportService.GetReportById(request)

# Retorna todos os reports de uma determinada localização, para gerar o mapa de calor
@app.route('/api/getReportByLocation', methods=['GET'])
def GetReportByLocation():
    return ReportService.GetReportByLocation(request)

@app.route('/api/insertReport', methods=['POST'])
def InsertReport():
    return ReportService.InsertReport(request)
