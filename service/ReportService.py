# Responsável por receber as requisições de report e encaminhar para o DAO

from flask import jsonify, Request, Response
from dao import reportsDao
from model.reportsModel import Reports as Report

# Recupera todos os reports do banco de dados
def GetAllReports() -> Response:
    # Solicita à dao todos os reports
    reports = reportsDao.GetAllReports()
    # Converte cada resultado para um dicionário, para facilitar a conversão para JSON
    reports_list = [r.__dict__() for r in reports]
    # Retorna a lista de reports em formato JSON
    return jsonify(reports_list)


# Recupera o id de um report a partir da query string e solicita o report ao DAO
def GetReportById(request: Request) -> str:
    # Recupera o id do report nos argumentos da request
    id = request.args.get('id')
    # Chama a função da DAO que recupera o report no banco de dados
    report = reportsDao.GetReportById(id)
    # Se o report não existir, retorna uma mensagem de erro
    if report is None:
        return jsonify({'msg': 'Don\'t exist'})
    # se o report existir, retorna o report em formato JSON
    else:
        return jsonify(report.__dict__())

# Recupera o location de um report a partir da query string e solicita o report ao DAO
def GetReportByLocation(request: Request) -> str:
    # Recupera o location do report nos argumentos do body da request
    location = request.args.get('location')
    # Chama a função da DAO que recupera o report no banco de dados
    report = reportsDao.GetReportByLocation(location)
    # Se o report não existir, retorna uma mensagem de erro
    if report is None:
        return jsonify({'msg': 'Don\'t exist'})
    # se o report existir, retorna o report em formato JSON
    else:
        return jsonify(report.__dict__())
    
# Insere um report vindo do front-end no banco de dados
def InsertReport(request) -> Response:
    # Cria um objeto do tipo Report com os dados do body request
    r = Report(Id=0, ReporterName=request.json['reporter_name'],
             Description=request.json['description'], OperationField=request.json['operation_field'],
             Location=request.json['location'],)
    # Chama a função da DAO que insere o report no banco de dados
    return reportsDao.InsertReport(r)