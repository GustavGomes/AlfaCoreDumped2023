# Insert
# Get

import mysql.connector
from dao import dao
from model import areasModel as area
from flask import Response

# Recupera uma área dado um id
def GetAreaById(id: int) -> area:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = "SELECT * FROM area WHERE Id = %s"
    # Mescla a query com o id passado como parâmetro e executa
    cursor.execute(query, (id,))
    # Se a query retornar apenas uma linha, cria um objeto do tipo Area e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Cria um objeto do tipo Area e retorna
            return area.Areas(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Recupera uma área dado um código
def GetAreaByCode(code: str) -> area:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = "SELECT * FROM area WHERE Code = %s"
    # Mescla a query com o código passado como parâmetro e executa
    cursor.execute(query, (code,))
    # Se a query retornar apenas uma linha, cria um objeto do tipo Area e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Cria um objeto do tipo Area e retorna
            return area.Area(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Insere uma área no banco de dados
def InsertArea(a: area) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        INSERT INTO area (id, code, description, liberation_status, pdf_path) 
        VALUES (%s,%s,%s,%s,%s);
        '''
    # Dados a serem passados para a query
    data = (a.Id, a.Code, a.Description, a.LiberationStatus, a.PdfFile)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Salva as alterações no banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo Area
    return Response(status=200)