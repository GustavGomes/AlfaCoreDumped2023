# Autores: Fernanda Mendes, Gustavo Gomes, Pedro Pampolini
# Sistema desenvolvido durante o Hackathon da Alfa Engenharia em 2023 
# O sistema segue o modelo de Service-DAO-Model:
# Model contém os modelos de dados representador no banco de dados
# DAO contém as funções de acesso ao banco de dados, com as queries necessárias
# Service contém as funções que são chamadas pelas rotas, e que chamam as funções do DAO,
# Service realiza algum tratamento prévio, como recuperar elementos do request

import os
from flask import Flask, jsonify, request, flash, redirect, url_for
import Utils
from service import UserService, AreasService, EquipmentsService, CandidateService, ReportService,RescissionSolicitationService, VacationSolicitationService
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = './Media/PDF/CPF/'

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
    print("InsertCandidate request received")
    return CandidateService.InsertCandidate(request)

@app.route('/api/getCandidates', methods=['GET'])
def GetCandidates():
    print("GetCandidates request received")
    return CandidateService.GetCandidates()

@app.route('/api/getCandidateById', methods=['GET'])
def GetCandidateById():
    return CandidateService.GetCandidateById(request)

@app.route('/api/approveCandidate', methods=['POST'])
def ApproveCandidate():
    print("Approve Candidate")
    return CandidateService.ApproveCandidate(request)


#-----------Reports----------------
@app.route('/api/getReportById', methods=['GET'])
def GetReportById():
    c = ReportService.GetReportById(request)
    print(c)
    return c
@app.route('/api/getReportByLocation', methods=['GET'])
def GetReportByLocation():
    return ReportService.GetReportByLocation(request)

@app.route('/api/insertReport', methods=['POST'])
def InsertReport():
    print("InsertReport request received")
    return ReportService.InsertReport(request)

@app.route('/api/getReports', methods=['GET'])
def GetReports():
    print("GetReports request received")
    return ReportService.GetAllReports()

#------------ Solicitação de férias ----------------

@app.route('/api/getVacationSolicitations', methods=['GET'])
def GetVacationSolicitations():
    print("GetVacationSolicitations request received")
    return VacationSolicitationService.GetVacationSolicitations()

@app.route('/api/getVacationSolicitationById', methods=['GET'])
def GetVacationSolicitationById():
    print("GetVacationSolicitationById request received")
    return VacationSolicitationService.GetVacationSolicitationById(request)

@app.route('/api/insertVacationSolicitation', methods=['POST'])
def InsertVacationSolicitation():
    print("InsertVacationSolicitation request received")
    return VacationSolicitationService.InsertVacationSolicitation(request)

#------------ Solicitação de recisão ----------------

@app.route('/api/getRescissionSolicitations', methods=['GET'])
def GetRescissionSolicitations():
    print("GetRescissionSolicitations request received")
    return RescissionSolicitationService.GetRescissionSolicitations()

@app.route('/api/getRescissionSolicitationById', methods=['GET'])
def GetRescissionSolicitationById():
    print("GetRescissionSolicitationById request received")
    return RescissionSolicitationService.GetRescissionSolicitationById(request)

@app.route('/api/insertRescissionSolicitation', methods=['POST'])
def InsertRescissionSolicitation():
    print("InsertRescissionSolicitation request received")
    return RescissionSolicitationService.InsertRescissionSolicitation(request)
#----------- Files ----------------
@app.route('/api/uploadFile', methods=['POST'])
def UploadFile():
    print("UploadFile request received")
    return Utils.UploadFile(request)