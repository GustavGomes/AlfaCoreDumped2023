from flask import jsonify, Request, Response
from dao import areasDao
from model.areasModel import Areas as Area

#Retorna uma area dada um ID
def GetAreaById(request: Request) -> str:
    # Recupera o id da área nos argumentos da request
    id = request.args.get('id')
    # Solicita à dao a área com o id recebido
    area = areasDao.GetAreaById(id)
    # Se a área não existir, retorna uma mensagem de erro
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    # Se a área existir, retorna a área em formato JSON
    else:
        return jsonify(area.__dict__())

#Retorna uma area dada um código
def GetAreaByCode(request: Request) -> str:
    # Recupera o código da área nos argumentos da request
    code = request.args.get('code')
    # Solicita à dao a área com o código recebido
    area = areasDao.GetAreaByCode(code)
    # Se a área não existir, retorna uma mensagem de erro
    if area is None:
        return jsonify({'msg': 'Don\'t exist'})
    # Se a área existir, retorna a área em formato JSON
    else:
        return jsonify(area.__dict__())

# Insere uma área vinda do front-end no banco de dados
def InsertArea(request) -> Response:
    # Cria um objeto do tipo Area com os dados do body request
    a = Area(Id=request.json['id'], Code=request.json['code'],
             Description=request.json['description'], LiberationStatus=request.json['liberationStatus'],
             PdfFile=request.json['pdfFile'])
    # Chama a função da DAO que insere a área no banco de dados
    return areasDao.InsertArea(a)