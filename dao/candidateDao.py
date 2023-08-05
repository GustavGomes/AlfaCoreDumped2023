import mysql.connector
from dao import dao
from model import candidatesModel as candidate
from flask import Response, jsonify

def GetCandidates() -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        SELECT * FROM candidate
        '''
    cursor.execute(query)
    ret_list = []

    for row in cursor:
        ret_list.append(candidate.Candidate(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41]))

    connection.close()
    return ret_list

def GetCandidateById(id: int) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        SELECT * FROM candidate WHERE id = %s
        '''
    data = (id,)
    cursor.execute(query, data)
    if cursor.arraysize == 1:
        try:
            row = cursor.fetchone()
            print(row)
            return candidate.Candidate(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41])
        except:
            pass
    connection.close()
    return None

def InsertCandidate(c: candidate) -> Response:
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    query = '''
        INSERT INTO candidate (id, name, mother_name, father_name, genre, civil_state, education_level, ethnicity, birth_date, nacionality, birth_country, birth_state, birth_city, shoe_size, pants_size, shirt_size, telephone_number, second_telephone_number, email, cep, country, state, city, neighborhood, residency_type, street, residency_number, complement, rg_number, rg_emissor_city, rg_release_date, cpf, pispasep, `function`, lodged, pcd, rg_file_path, cpf_file_path, resume_file_path, cnh_file_path, army_file_path, has_friend_familiar)
        Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
    data = (c.id, c.CandidateName, c.MotherName, c.FatherName, c.Gender, c.CiviState, c.EducationLevel, c.Ethnicity, c.BirthDate, c.Nacionality, c.BirthCountry, c.BirthState, c.BirthCity, c.ShoeSize, c.PantsSize, c.ShirtSize, c.TelephoneNumber, c.SecondTelephoneNumber, c.Email, c.Cep, c.Country, c.State, c.City, c.Neighborhood, c.ResidencyType, c.Street, c.ResidencyNumber, c.Complement, c.RgNumber, c.RgEmissorCity, c.RgReleaseDate, c.Cpf, c.Pispasep, c.Function, c.Lodged, c.Pcd, c.RgFile, c.CpfFile, c.ResumeFile, c.CnhFile, c.ArmyFile, c.HasFriendFamiliar)
    cursor.execute(query, data)
    connection.commit()
    connection.close()
    return Response(status=200)