from flask import jsonify, Request, Response
from dao import equipmentsDao
from model.areasModel import Areas as Area

def GetEquipmentById(request: Request) -> str:
    #id = request.json['id']
    id = request.args.get('id')
    area = equipmentsDao.GetEquipmentById(id)
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(area.__dict__())
    
def GetEquipmentByCode(request: Request) -> str:
    #code = request.json['code']
    code = request.args.get('code')
    area = equipmentsDao.GetEquipmentByCode(code)
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(area.__dict__())
    
def InsertEquipment(request) -> Response:
    a = Area(Id=request.json['id'], Code=request.json['code'],
             Description=request.json['description'], LiberationStatus=request.json['liberationStatus'],
             PdfFile=request.json['pdfFile'])
    return equipmentsDao.InsertEquipment(a)