import mysql.connector
from dao import dao
from model import rescissionSolicitationModel as rescissionSolicitation
from flask import Response, jsonify

# Retorna uma lista de todas as solicitações de rescisão
def GetRescissionSolicitations() -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        SELECT * FROM rescissionsolicitation
        '''
    # Executa a query
    cursor.execute(query)
    # Cria uma lista vazia para armazenar as solicitações de rescisão que serão retornadas
    ret_list = []
    # Para cada linha retornada pela query, cria um objeto do tipo RescissionSolicitation e adiciona na lista
    for row in cursor:
        ret_list.append(rescissionSolicitation.RescissionSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna a lista de solicitações de rescisão
    return ret_list

# Retorna uma solicitação de rescisão dado um id
def GetRescissionSolicitationById(id: int) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        SELECT * FROM rescissionsolicitation WHERE id = %s
        '''
    # Dados a serem passados para a query
    data = (id,)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Se a query retornar apenas uma linha, cria um objeto do tipo RescissionSolicitation e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Retorna o objeto do tipo RescissionSolicitation
            return rescissionSolicitation.RescissionSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

#Insere uma solicitação de rescisão no banco de dados
def InsertRescissionSolicitation(r: rescissionSolicitation) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        INSERT INTO rescissionsolicitation (id, creator_id, target_id, status,`rank`, reason, description, creation_date, start_date, end_date, user_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
    # Dados a serem passados para a query
    data = (r.id, r.CreatorId, r.TargetId, r.Status, r.Rank, r.Reason, r.Description, r.CreationDate, r.StartDate, r.EndDate, r.UserId)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Salva as alterações no banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo RescissionSolicitation
    return Response(status=200)