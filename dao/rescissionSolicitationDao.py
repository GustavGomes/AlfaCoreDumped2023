import mysql.connector
from dao import dao
from model import rescissionSolicitationModel as rescissionSolicitation
from flask import Response, jsonify

def GetRescissionSolicitations() -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        SELECT * FROM rescissionsolicitation
        '''
    cursor.execute(query)
    ret_list = []

    for row in cursor:
        ret_list.append(rescissionSolicitation.RescissionSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    connection.close()
    return ret_list

def GetRescissionSolicitationById(id: int) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        SELECT * FROM rescissionsolicitation WHERE id = %s
        '''
    data = (id,)
    cursor.execute(query, data)
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            return rescissionSolicitation.RescissionSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        except:
            pass
    connection.close()
    return None

def InsertRescissionSolicitation(r: rescissionSolicitation) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        INSERT INTO rescissionsolicitation (id, creator_id, target_id, status,`rank`, reason, description, creation_date, start_date, end_date, user_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
    data = (r.id, r.CreatorId, r.TargetId, r.Status, r.Rank, r.Reason, r.Description, r.CreationDate, r.StartDate, r.EndDate, r.UserId)
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)