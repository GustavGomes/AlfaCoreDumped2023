from flask import jsonify, Request, Response
from dao import vacationSolicitationDao
from model.vacationSolicitationModel import VacationSolicitation

# Insere no banco uma solicitação de férias pela DAO
def InsertVacationSolicitation(request) -> Response:
    # Cria um objeto do tipo VacationSolicitation com os dados do request
    v = VacationSolicitation(id=request.json['id'], CreatorId=request.json['creatorId'], TargetId=request.json['targetId'], Status=request.json['status'], VacationStart=request.json['vacationStart'], VacationEnd=request.json['vacationEnd'], Description=request.json['description'], CreationDate=request.json['creationDate'], StartDate=request.json['startDate'], EndDate=request.json['endDate'], UserId=request.json['userId'])
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
