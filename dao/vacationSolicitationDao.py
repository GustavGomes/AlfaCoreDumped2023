import mysql.connector
from dao import dao
from model import vacationSolicitationModel as vacationSolicitation
from flask import Response, jsonify

# Retorna uma lista de todas as solicitações de férias
def GetVacationSolicitations() -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        SELECT * FROM vacationsolicitation
        '''
    # Executa a query
    cursor.execute(query)
    # Cria uma lista vazia para armazenar as solicitações de férias que serão retornadas
    ret_list = []
    # Para cada linha retornada pela query, cria um objeto do tipo VacationSolicitation e adiciona na lista
    for row in cursor:
        ret_list.append(vacationSolicitation.VacationSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna a lista de solicitações de férias
    return ret_list

# Retorna uma solicitação de férias dado um id
def GetVacationSolicitationById(id: int) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        SELECT * FROM vacationsolicitation WHERE id = %s
        '''
    # Dados a serem passados para a query
    data = (id,)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Se a query retornar apenas uma linha, cria um objeto do tipo VacationSolicitation e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query 
            row = cursor.fetchone()
            # Retorna o objeto do tipo VacationSolicitation
            return vacationSolicitation.VacationSolicitation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Retorna uma lista de solicitações de férias dado um id de usuário
def InsertVacationSolicitation(v: vacationSolicitation) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        INSERT INTO vacationsolicitation (id, creatorid, targetid, status, vacation_start, vacation_end, description, creation_date, start_date, end_date, user_id)
        Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
    # Dados a serem passados para a query
    data = (v.id, v.CreatorId, v.TargetId, v.Status, v.VacationStart, v.VacationEnd, v.Description, v.CreationDate, v.StartDate, v.EndDate, v.UserId)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Salva as alterações no banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna uma resposta de sucesso
    return Response(status=200)