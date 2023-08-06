import mysql.connector
from dao import dao
from model import userModel as user
from flask import Response

# Realiza o login de um usuário dado um cpf e uma senha
def Login(cpf, Password) -> user:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = "SELECT * FROM user WHERE cpf = %s AND password = %s"
    # Dados a serem passados para a query
    cursor.execute(query, (cpf, Password))
    
    # Se a query retornar apenas uma linha, cria um objeto do tipo User e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Retorna o objeto do tipo User
            return user.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Retorna uma lista de todos os usuários
def InsertUser(u: user) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        INSERT INTO user (Id, UserName, Password, Cpf, Gender, Role, RoleId, Cbo, Permission) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
        '''
    # Dados a serem passados para a query
    data = (u.Id, u.Username, u.Password, u.Cpf, u.Gender
            , u.RoleName, u.RoleId, u.Cbo,u.Permission)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Fecha a conexão com o banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo User
    return Response(status=200)

# Atualiza um usuário no banco de dados
def UpdateUser(u: user) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        UPDATE user
        SET Username = %s,
            Password = %s,
            Cpf = %s,
            Gender = %s,
            Role = %s,
            RoleId = %s,
            Cbo = %s,
            Permission = %s
        WHERE Id = %s;
        '''
    # Dados a serem passados para a query
    data = (u.Username, u.Password, u.Cpf, u.Gender
            , u.RoleName, u.RoleId, u.Cbo, u.Permission ,u.Id)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Salva as alterações no banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo User
    return Response(status=200)

# Deleta um usuário do banco de dados
def DeleteUser(Id: int) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        DELETE FROM user
        WHERE Id = %s;
        '''
    # Executa a query mesclando-a com os dados
    cursor.execute(query, (Id,))
    # Salva as alterações no banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo User
    return Response(status=200)