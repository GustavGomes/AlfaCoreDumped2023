# Insert
# Get

import mysql.connector
from dao import dao
from model import areasModel as area
from flask import Response

def GetAreaById(id: int) -> area:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = "SELECT * FROM area WHERE Id = %s"
    cursor.execute(query, (id,))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            print(row)
            return area.Areas(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    connection.close()
    return None

def GetAreaByCode(code: str) -> area:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = "SELECT * FROM area WHERE Code = %s"
    cursor.execute(query, (code,))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            return area.Area(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    connection.close()
    return None

def InsertArea(a: area) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        INSERT INTO area (id, code, description, liberation_status, pdf_path) 
        VALUES (%s,%s,%s,%s,%s);
        '''
    data = (a.Id, a.Code, a.Description, a.LiberationStatus, a.PdfFile)
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)