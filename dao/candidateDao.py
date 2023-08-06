import mysql.connector
from dao import dao
from model import candidatesModel as candidate
from flask import Response, jsonify

# Retorna uma lista de todos os candidatos
def GetCandidates() -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        SELECT * FROM candidate
        '''
    # Executa a query
    cursor.execute(query)
    # Cria uma lista vazia para armazenar os candidatos que serão retornados
    ret_list = []
    # Para cada linha retornada pela query, cria um objeto do tipo Candidate e adiciona na lista
    for row in cursor:
        ret_list.append(candidate.Candidate(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41]))
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna a lista de candidatos
    return ret_list

# Retorna um candidato dado um id
def GetCandidateById(id: int) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        SELECT * FROM candidate WHERE id = %s
        '''
    # Dados a serem passados para a query
    data = (id,)
    # Executa a query mesclando-a com os dados, ou seja, o id passado
    cursor.execute(query, data)
    # Se a query retornar apenas uma linha, cria um objeto do tipo Candidate e retorna
    if cursor.arraysize == 1:
        try:
            # Recupera a única linha retornada pela query
            row = cursor.fetchone()
            # Retorna o objeto do tipo Candidate
            return candidate.Candidate(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41])
        except:
            pass
    # Fecha a conexão com o banco de dados
    connection.close()
    # Se a query retornar mais de uma linha, retorna Null
    return None

# Insere um candidato no banco de dados
def InsertCandidate(c: candidate) -> Response:
    # Abre a conexão com o banco de dados
    connection = dao.OpenConnection()
    # Cria um cursor para executar as queries sql
    cursor = connection.cursor()
    # Query a ser executada
    query = '''
        INSERT INTO candidate (name, mother_name, father_name, genre, civil_state, education_level, ethnicity, birth_date, nacionality, birth_country, birth_state, birth_city, shoe_size, pants_size, shirt_size, telephone_number, second_telephone_number, email, cep, country, state, city, neighborhood, residency_type, street, residency_number, complement, rg_number, rg_emissor_city, rg_release_date, cpf, pispasep, `function`, lodged, pcd, rg_file_path, cpf_file_path, resume_file_path, cnh_file_path, army_file_path, has_friend_familiar)
        Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
    # Dados a serem passados para a query
    data = (c.CandidateName, c.MotherName, c.FatherName, c.Gender, c.CiviState, c.EducationLevel, c.Ethnicity, c.BirthDate, c.Nacionality, c.BirthCountry, c.BirthState, c.BirthCity, c.ShoeSize, c.PantsSize, c.ShirtSize, c.TelephoneNumber, c.SecondTelephoneNumber, c.Email, c.Cep, c.Country, c.State, c.City, c.Neighborhood, c.ResidencyType, c.Street, c.ResidencyNumber, c.Complement, c.RgNumber, c.RgEmissorCity, c.RgReleaseDate, c.Cpf, c.Pispasep, c.Function, c.Lodged, c.Pcd, c.RgFile, c.CpfFile, c.ResumeFile, c.CnhFile, c.ArmyFile, c.HasFriendFamiliar)
    # Executa a query mesclando-a com os dados
    cursor.execute(query, data)
    # Fecha a conexão com o banco de dados
    connection.commit()
    # Fecha a conexão com o banco de dados
    connection.close()
    # Retorna o objeto do tipo Candidate
    return Response(status=200)