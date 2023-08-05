from flask import jsonify, Request, Response
from dao import reportsDao
from model.reportsModel import Reports as Report

def GetReportById(request: Request) -> str:
    #id = request.json['id']
    id = request.args.get('id')
    area = reportsDao.GetReportById(id)
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(area.__dict__())
    
def GetReportByLocation(request: Request) -> str:
    #code = request.json['code']
    location = request.args.get('location')
    report = reportsDao.GetReportByLocation(location)
    if report is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(report.__dict__())
    
def InsertReport(request) -> Response:
    r = Report(Id=request.json['id'], ReporterName=request.json['reporterName'],
             Description=request.json['description'], OperationField=request.json['operationField'],
             CreatedAt=request.json['createdAt'],Location=request.json['location'],
             images=[request.json['images'][0], request.json['images'][1], request.json['images'][2]])
    return reportsDao.InsertReport(r)