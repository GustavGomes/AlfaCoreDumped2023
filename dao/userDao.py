import mysql.connector
from dao import dao
from model import userModel as user
from flask import Response

def GetAllUser():
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    for row in cursor:
        print("Row: ", row)

    connection.close()

def Login(cpf, Password) -> user:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = "SELECT * FROM user WHERE cpf = %s AND password = %s"
    cursor.execute(query, (cpf, Password))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            return user.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8])
        except:
            pass
    connection.close()
    return None

def InsertUser(u: user) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        INSERT INTO user (Id, UserName, Password, Cpf, Gender, Role, RoleId, Cbo, Permission) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
        '''
    data = (u.Id, u.Username, u.Password, u.Cpf, u.Gender
            , u.RoleName, u.RoleId, u.Cbo)
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)

def UpdateUser(u: user) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
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
    print(u.Gender)
    print(query)
    data = (u.Username, u.Password, u.Cpf, u.Gender
            , u.RoleName, u.RoleId, u.Cbo, u.Permission ,u.Id)
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)

def DeleteUser(Id: int) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        DELETE FROM user
        WHERE Id = %s;
        '''
    cursor.execute(query, (Id,))
    connection.commit()
    connection.close()
    return Response(status=200)