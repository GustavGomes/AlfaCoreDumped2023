from flask import jsonify, Request, Response
from dao import vacationSolicitationDao
from model.vacationSolicitationModel import VacationSolicitation

# Recupera todos os reports do banco de dados
def GetAllVacations() -> Response:
    # Solicita à dao todos os reports
    reports = vacationSolicitationDao.GetAllVacations()
    # Converte cada resultado para um dicionário, para facilitar a conversão para JSON
    reports_list = [r.__dict__() for r in reports]
    # Retorna a lista de reports em formato JSON
    return jsonify(reports_list)

# Insere no banco uma solicitação de férias pela DAO
def InsertVacationSolicitation(request) -> Response:
    # Cria um objeto do tipo VacationSolicitation com os dados do request
    v = VacationSolicitation(id=0, CreatorId=request.json['creator_id'], TargetId=0, Status=request.json['status'], VacationStart=request.json['vacation_start'], VacationEnd=request.json['vacation_end'], Description=request.json['description'], CreationDate=request.json['creation_date'], StartDate=request.json['start_date'], EndDate=request.json['end_date'], UserId=0)
    
    #Trata as dadas
    v.CreationDate = v.CreationDate[0:10]
    v.StartDate = v.StartDate[0:10]
    v.EndDate = v.EndDate[0:10]
    v.VacationStart = v.VacationStart[0:10]
    v.VacationEnd = v.VacationEnd[0:10]
    
    # retorna o resultado da função da DAO, caso positivo tem status 200
    return vacationSolicitationDao.InsertVacationSolicitation(v)

# Recupera no banco uma solicitação de férias pela DAO
def GetVacationSolicitations() -> Response:
    # Solicita à dao todas as solicitações de férias
    vacations = vacationSolicitationDao.GetVacationSolicitations()
    # Converte cada resultado para um dicionário, para facilitar a conversão para JSON
    vacations_list = [r._dict_() for r in vacations]
    # Retorna a lista de solicitações de férias em formato JSON
    return jsonify(vacations_list)

# Recupera no banco uma solicitação de férias pela DAO
def GetVacationSolicitationById(request) -> Response:
    # Recupera o id da solicitação de férias nos argumentos da request
    id = request.args.get('id')
    # Retorna a solicitação de férias em formato JSON
    return jsonify(vacationSolicitationDao.GetVacationSolicitationById(id)._dict_())
