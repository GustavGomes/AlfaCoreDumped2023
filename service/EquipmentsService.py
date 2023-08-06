# Responsável por receber as requisições de equipamentos e encaminhar para o DAO

from flask import jsonify, Request, Response
from dao import equipmentsDao
from model.equipmentsModel import Equipment

# Retorna um equipamento a partir do id
def GetEquipmentById(request: Request) -> str:
    # Cria o id com o valor do argumento da request
    id = request.args.get('id')
    # Solicita à dao o equipamento com o id recebido
    equipment = equipmentsDao.GetEquipmentById(id)
    # Se o equipamento não existir, retorna uma mensagem de erro
    if equipment is None:
        return jsonify({'msg': 'Don\'t exist'})
    # Se o equipamento existir, retorna o equipamento em formato JSON
    else:
        return jsonify(equipment.__dict__())

# Retorna um equipamento a partir do código dele
def GetEquipmentByCode(request: Request) -> str:
    # Cria o code com o valor do argumento da request
    code = request.args.get('code')
    # Solicita à dao o equipamento com o code recebido
    equipment = equipmentsDao.GetEquipmentByCode(code)
    # Se o equipamento não existir, retorna uma mensagem de erro
    if equipment is None:
        return jsonify({'msg': 'Don\'t exist'})
    # Se o equipamento existir, retorna o equipamento em formato JSON
    else:
        return jsonify(equipment.__dict__())

# Insere um equipamento vindo do front-end no banco de dados
def InsertEquipment(request) -> Response:
    # Cria um objeto do tipo Equipment com os dados do body request
    a = Equipment(Id=request.json['id'], Code=request.json['code'],
             Description=request.json['description'], LiberationStatus=request.json['liberationStatus'],
             PdfFile=request.json['pdfFile'])
    # Chama a função da DAO que insere o equipamento no banco de dados
    return equipmentsDao.InsertEquipment(a)