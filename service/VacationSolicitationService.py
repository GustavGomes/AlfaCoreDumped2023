from flask import jsonify, Request, Response
from dao import vacationSolicitationDao
from model.vacationSolicitationModel import VacationSolicitation


def InsertVacationSolicitation(request) -> Response:
    v = VacationSolicitation(id=request.json['id'], CreatorId=request.json['creatorId'], TargetId=request.json['targetId'], Status=request.json['status'], VacationStart=request.json['vacationStart'], VacationEnd=request.json['vacationEnd'], Description=request.json['description'], CreationDate=request.json['creationDate'], StartDate=request.json['startDate'], EndDate=request.json['endDate'], UserId=request.json['userId'])
    return vacationSolicitationDao.InsertVacationSolicitation(v)

def GetVacationSolicitations() -> Response:
    vacations = vacationSolicitationDao.GetVacationSolicitations()
    vacations_list = [r._dict_() for r in vacations]
    return jsonify(vacations_list)

def GetVacationSolicitationById(request) -> Response:
    id = request.args.get('id')
    return jsonify(vacationSolicitationDao.GetVacationSolicitationById(id)._dict_())
