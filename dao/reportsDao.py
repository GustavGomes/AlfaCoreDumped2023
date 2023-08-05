from dao import dao
from model import reportsModel as report
from flask import Response

def GetReportById(id: int) -> report:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = "SELECT * FROM report WHERE Id = %s"
    cursor.execute(query, (id,))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            return report.Reports(row[0], row[1], row[2], row[3], row[4], row[5], row[6], [row[7], row[8], row[9]])
        except:
            pass
    connection.close()
    return None

def GetAreaByLocation(location: str) -> area:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = "SELECT * FROM report WHERE location = %s"
    cursor.execute(query, (location,))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            return report.Reports(row[0], row[1], row[2], row[3], row[4], row[5], row[6], [row[7], row[8], row[9]])
        except:
            pass
    connection.close()
    return None

def InsertReport(r: report.Reports) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        INSERT INTO report (id, reporter_name, cost_center, description, creation_date, location, picture_one_path, picture_two_path, picture_three_path) 
        VALUES (%s,%s,%s,%s,%s);
        '''
    data = (r.Id, r.ReporterName, r.CostCenter, r.Description, r.OperationField, r.CreatedAt, r.Location, r.images[0], r.images[1], r.images[2])
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)# Insert
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
            return area.Area(row[0], row[1], row[2], row[3], row[4])
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