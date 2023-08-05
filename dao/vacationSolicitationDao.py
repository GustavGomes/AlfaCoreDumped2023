import mysql.connector
from dao import dao
from model import vacationSolicitationModel as vacationSolicitation
from flask import Response, jsonify

def GetVacationSolicitations() -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        SELECT * FROM vacationsolicitation
        '''
    cursor.execute(query)
    ret_list = []
    for row in cursor:
        ret_list.append(vacationSolicitation.VacationSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    connection.close()

    return ret_list

def GetVacationSolicitationById(id: int) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        SELECT * FROM vacationsolicitation WHERE id = %s
        '''
    data = (id,)
    cursor.execute(query, data)
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            return vacationSolicitation.VacationSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        except:
            pass
    connection.close()
    return None

def InsertVacationSolicitation(v: vacationSolicitation) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        INSERT INTO vacationsolicitation (id, creatorid, targetid, status, vacation_start, vacation_end, description, creation_date, start_date, end_date, user_id)
        Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
    data = (v.id, v.CreatorId, v.TargetId, v.Status, v.VacationStart, v.VacationEnd, v.Description, v.CreationDate, v.StartDate, v.EndDate, v.UserId)
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)