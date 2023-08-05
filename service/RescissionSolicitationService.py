from flask import jsonify, Request, Response
from dao import rescissionSolicitationDao
from model.rescissionSolicitationModel import RescissionSolicitation


def InsertRescissionSolicitation(request) -> Response:
    s = RescissionSolicitation(id=request.json['id'], CreatorId=request.json['creatorId'], TargetId=request.json['targetId'], Status=request.json['status'], Rank=request.json['rank'], Reason=request.json['reason'], Description=request.json['description'], CreationDate=request.json['creationDate'], StartDate=request.json['startDate'], EndDate=request.json['endDate'], UserId=request.json['userId'])
    return rescissionSolicitationDao.InsertRescissionSolicitation(s)

def GetRescissionSolicitations() -> Response:
    rescissions = rescissionSolicitationDao.GetRescissionSolicitations()
    rescissions_list = [r._dict_() for r in rescissions]
    return jsonify(rescissions_list)

def GetRescissionSolicitationById(request) -> Response:
    id = request.args.get('id')
    return jsonify(rescissionSolicitationDao.GetRescissionSolicitationById(id)._dict_())

