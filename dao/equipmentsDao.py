# Insert
# Get

from dao import dao
from model import equipmentsModel as equipment
from flask import Response

# Recupera um equipamento dado um id
def GetEquipmentById(id: int) -> equipment:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = "SELECT * FROM equipment WHERE Id = %s"
    # Mescla a query com o id passado como parâmetro
    cursor.execute(query, (id,))
    # Se a query retornar apenas uma linha, cria um objeto do tipo Equipment e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Cria um objeto do tipo Equipment e retorna
            return equipment.Equipment(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Recupera um equipamento dado um código
def GetEquipmentByCode(code: str) -> equipment:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = "SELECT * FROM equipment WHERE Code = %s"
    # Mescla a query com o código passado como parâmetro e executa
    cursor.execute(query, (code,))
    # Se a query retornar apenas uma linha, cria um objeto do tipo Equipment e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Cria um objeto do tipo Equipment e retorna
            return equipment.Equipment(row[0], row[1], row[2], row[3], row[4])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Insere um equipamento no banco de dados
def InsertEquipment(a: equipment) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        INSERT INTO equipment (code, description, liberation_status, pdf_path) 
        VALUES (%s,%s,%s,%s);
        '''
    # Dados a serem passados para a query
    data = (a.Code, a.Description, a.LiberationStatus, a.PdfFile)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Salva as alterações no banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo Equipment
    return Response(status=200)