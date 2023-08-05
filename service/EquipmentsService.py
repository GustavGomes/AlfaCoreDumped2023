# Responsável por receber as requisições de equipamentos e encaminhar para o DAO

from flask import jsonify, Request, Response
from dao import equipmentsDao
from model.equipmentsModel import Equipment

# Retorna um equipamento a partir do id
def GetEquipmentById(request: Request) -> str:
    #id = request.json['id']
    id = request.args.get('id')
    area = equipmentsDao.GetEquipmentById(id)
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(area.__dict__())

# Retorna um equipamento a partir do código dele
def GetEquipmentByCode(request: Request) -> str:
    #code = request.json['code']
    code = request.args.get('code')
    area = equipmentsDao.GetEquipmentByCode(code)
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    else:
        return jsonify(area.__dict__())

# Insere um equipamento vindo do front-end no banco de dados
def InsertEquipment(request) -> Response:
    a = Equipment(Id=request.json['id'], Code=request.json['code'],
             Description=request.json['description'], LiberationStatus=request.json['liberationStatus'],
             PdfFile=request.json['pdfFile'])
    return equipmentsDao.InsertEquipment(a)