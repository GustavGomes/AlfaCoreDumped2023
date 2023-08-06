from flask import jsonify, Request, Response
from dao import rescissionSolicitationDao
from model.rescissionSolicitationModel import RescissionSolicitation

# Insere no banco uma solicitação de rescisão pela DAO
def InsertRescissionSolicitation(request) -> Response:
    # Cria um objeto do tipo RescissionSolicitation com os dados do request
    s = RescissionSolicitation(id=0, CreatorId=request.json['creator_id'], TargetId=request.json['target_id'], Status=request.json['status'], Rank=request.json['rank'], Reason=request.json['reason'], Description=request.json['description'], CreationDate=request.json['creation_date'], StartDate=request.json['start_date'], EndDate=request.json['end_date'], UserId=request.json['user_id'])
    # retorna o resultado da função da DAO, caso positivo tem status 200
    return rescissionSolicitationDao.InsertRescissionSolicitation(s)

# Recupera no banco uma solicitação de rescisão pela DAO
def GetRescissionSolicitations() -> Response:
    # Solicita à dao todas as solicitações de rescisão
    rescissions = rescissionSolicitationDao.GetRescissionSolicitations()
    # Converte cada resultado para um dicionário, para facilitar a conversão para JSON
    rescissions_list = [r._dict_() for r in rescissions]
    # Retorna a lista de solicitações de rescisão em formato JSON
    return jsonify(rescissions_list)

# Recupera no banco uma solicitação de rescisão pela DAO
def GetRescissionSolicitationById(request) -> Response:
    # Recupera o id da solicitação de rescisão nos argumentos da request
    id = request.args.get('id')
    # Retorna a solicitação de rescisão em formato JSON
    return jsonify(rescissionSolicitationDao.GetRescissionSolicitationById(id)._dict_())

