# Responsável por receber as requisições do usuário e encaminhar para o DAO
# 

from flask import jsonify, Request, Response
from dao import userDao
from model.userModel import User

# Recupera o username e password do usuário e verifica se existe no banco de dados
# Se existir, retorna o usuário, se não, retorna uma mensagem de erro de credenciais inválidas
def Login(request: Request) -> str:
    username = request.json['cpf']
    password = request.json['password']
    user = userDao.Login(username, password)
    if user is None:
        return jsonify({'msg': 'Invalid Credentials'})
    else:
        return jsonify(user.__dict__())

# Insere um usuário no banco de dados, apenas para testes
def InsertUser(request) -> Response:
    u = User(Id=request.json['id'], Username=request.json['username'],
             Password=request.json['password'], Cpf=request.json['cpf'],
             Gender=request.json['gender'], RoleName=request.json['roleName'],
             RoleId=request.json['roleId'], Cbo=request.json['cbo'],Permission=request.json['permission'])
    return userDao.InsertUser(u)

def UpdateUser(request) -> Response:
    u = User(Id=request.json['id'], Username=request.json['username'],
             Password=request.json['password'], Cpf=request.json['cpf'],
             Gender=request.json['gender'], RoleName=request.json['roleName'],
             RoleId=request.json['roleId'], Cbo=request.json['cbo'])
    return userDao.UpdateUser(u)

def DeleteUser(request) -> Response:
    id = request.json['id']
    return userDao.DeleteUser(id)