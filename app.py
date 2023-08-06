# Autores: Fernanda Mendes, Gustavo Gomes, Pedro Pampolini
# Sistema desenvolvido durante o Hackathon da Alfa Engenharia em 2023 
# O sistema segue o modelo de Service-DAO-Model:
# Model contém os modelos de dados representador no banco de dados
# DAO contém as funções de acesso ao banco de dados, com as queries necessárias
# Service contém as funções que são chamadas pelas rotas, e que chamam as funções do DAO,
# Service realiza algum tratamento prévio, como recuperar elementos do request

import os
from flask import Flask, jsonify, request, flash, redirect, url_for
from service import UserService, AreasService, EquipmentsService, CandidateService, ReportService, UtilsService
from flask_cors import CORS
from werkzeug.utils import secure_filename

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


#-----------Reports----------------
@app.route('/api/getReportById', methods=['GET'])
def GetReportById():
    return ReportService.GetReportById(request)

@app.route('/api/getReportByLocation', methods=['GET'])
def GetReportByLocation():
    return ReportService.GetReportByLocation(request)

@app.route('/api/insertReport', methods=['POST'])
def InsertReport():
    return ReportService.InsertReport(request)

#----------- Files ----------------
@app.route('/api/uploadFile', methods=['POST'])
def UploadFile():
    print("UploadFile request received")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print("No file part")
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return 