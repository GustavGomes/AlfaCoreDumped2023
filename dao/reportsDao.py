from dao import dao
from model import reportsModel as report
from flask import Response

def GetReportById(id: int) -> report:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    print("kabakcsu:", type(id))
    query = "SELECT * FROM report WHERE id = %s"
    cursor.execute(query, (id,))
    
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            print("row:", row)
            return report.Reports(row[0], row[1], row[2], row[3], '', row[4], row[5], [row[6], row[7], row[8]])
            return report.Reports(row[0], row[1], row[2], row[3], row[4], row[5],[row[6], row[7], row[8]])
        except Exception as e:
            print("Error: ", e)
            pass
    connection.close()
    return None

def GetReportByLocation(location: str) -> report:
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
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
        '''
    data = (r.Id, r.ReporterName, r.CostCenter, r.Description, r.CreatedAt, r.Location, r.images[0], r.images[1], r.images[2])
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)
