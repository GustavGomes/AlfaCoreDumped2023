from dao import dao
from model import reportsModel as report
from flask import Response

def GetAllReports() -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        SELECT * FROM report
        '''
    # Executa a query
    cursor.execute(query)
    # Cria uma lista vazia para armazenar os relatórios que serão retornados
    ret_list = []
    # Para cada linha retornada pela query, cria um objeto do tipo Report e adiciona na lista
    for row in cursor:
        ret_list.append(report.Reports(row[0], row[1], row[2], row[3], '', row[4], row[5], [row[6], row[7], row[8]]))
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna a lista de relatórios
    return ret_list

# Retorna uma lista de todos os relatórios
def GetReportById(id: int) -> report:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = "SELECT * FROM report WHERE id = %s"
    # Dados a serem passados para a query
    cursor.execute(query, (id,))
    # Se a query retornar apenas uma linha, cria um objeto do tipo Report e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Retorna o objeto do tipo Report
            return report.Reports(row[0], row[1], row[2], row[3], '', row[4], row[5], [row[6], row[7], row[8]])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None


# Retorna uma lista de um relatório de um local
def GetReportByLocation(location: str) -> report:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = "SELECT * FROM report WHERE location = %s"
    # Dados a serem passados para a query
    cursor.execute(query, (location,))
    # Se a query retornar apenas uma linha, cria um objeto do tipo Report e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Retorna o objeto do tipo Report
            return report.Reports(row[0], row[1], row[2], row[3], row[4], row[5], row[6], [row[7], row[8], row[9]])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Insere um relatório no banco de dados
def InsertReport(r: report.Reports) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        INSERT INTO report (reporter_name, cost_center, description, creation_date, location, picture_one_path, picture_two_path, picture_three_path) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
        '''
    # Dados a serem passados para a query
    data = (r.ReporterName, r.CostCenter, r.Description, r.CreatedAt, r.Location, r.images[0], r.images[1], r.images[2])
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Salva as alterações no banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo Report
    return Response(status=200)
