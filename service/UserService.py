# Responsável por receber as requisições do usuário e encaminhar para o DAO
# 

from flask import jsonify, Request, Response
from dao import userDao
from model.userModel import User

# Recupera o username e password do usuário e verifica se existe no banco de dados
# Se existir, retorna o usuário, se não, retorna uma mensagem de erro de credenciais inválidas
def Login(request: Request) -> str:
    # Recupera o username e password do body da request
    username = request.json['cpf']
    password = request.json['password']
    # Chama a função da DAO que verifica as credenciais do usuário no banco de dados
    user = userDao.Login(username, password)
    # Se o usuário não existir, retorna uma mensagem de erro
    if user is None:
        return jsonify({'msg': 'Invalid Credentials'})
    # Se o usuário existir, retorna os dados do usuário em formato JSON
    else:
        return jsonify(user.__dict__())

# Insere um usuário no banco de dados, apenas para testes
def InsertUser(request) -> Response:
    # Cria um objeto do tipo User com os dados do request
    u = User(Id=request.json['id'], Username=request.json['username'],
             Password=request.json['password'], Cpf=request.json['cpf'],
             Gender=request.json['gender'], RoleName=request.json['roleName'],
             RoleId=request.json['roleId'], Cbo=request.json['cbo'],Permission=request.json['permission'])
    # Chama a função da DAO que insere o usuário no banco de dados
    return userDao.InsertUser(u)

# Atualiza o usuario no banco de dados
def UpdateUser(request) -> Response:
    # cria um objeto do tipo User com os dados do body da request
    u = User(Id=request.json['id'], Username=request.json['username'],
             Password=request.json['password'], Cpf=request.json['cpf'],
             Gender=request.json['gender'], RoleName=request.json['roleName'],
             RoleId=request.json['roleId'], Cbo=request.json['cbo'])
    # Chama a função da DAO que atualiza o usuário no banco de dados
    return userDao.UpdateUser(u)

# Deleta o usuario no banco de dados
def DeleteUser(request) -> Response:
    # Recupera o id do usuário nos argumentos da request
    id = request.json['id']
    # Chama a função da DAO que deleta o usuário no banco de dados
    return userDao.DeleteUser(id)