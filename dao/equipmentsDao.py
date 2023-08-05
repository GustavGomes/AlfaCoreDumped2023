# Insert
# Get

from dao import dao
from model import equipmentsModel as equipment
from flask import Response

def GetEquipmentById(id: int) -> equipment:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = "SELECT * FROM equipment WHERE Id = %s"
    cursor.execute(query, (id,))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            print("Row: ", row)
            return equipment.Equipment(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    connection.close()
    return None

def GetEquipmentByCode(code: str) -> equipment:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = "SELECT * FROM equipment WHERE Code = %s"
    cursor.execute(query, (code,))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            return equipment.Equipment(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    connection.close()
    return None

def InsertEquipment(a: equipment) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        INSERT INTO equipment (id, code, description, liberation_status, pdf_path) 
        VALUES (%s,%s,%s,%s,%s);
        '''
    data = (a.Id, a.Code, a.Description, a.LiberationStatus, a.PdfFile)
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)