from flask import jsonify, Request, Response
from dao import areasDao
from model.areasModel import Areas as Area

def GetAreaById(request: Request) -> str:
    #id = request.json['id']
    id = request.args.get('id')
    area = areasDao.GetAreaById(id)
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(area.__dict__())
    
def GetAreaByCode(request: Request) -> str:
    #code = request.json['code']
    code = request.args.get('code')
    area = areasDao.GetAreaByCode(code)
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(area.__dict__())
    
def InsertArea(request) -> Response:
    a = Area(Id=request.json['id'], Code=request.json['code'],
             Description=request.json['description'], LiberationStatus=request.json['liberationStatus'],
             PdfFile=request.json['pdfFile'])
    return areasDao.InsertArea(a)