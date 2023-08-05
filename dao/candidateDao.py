import mysql.connector
from dao import dao
from model import candidatesModel as candidate
from flask import Response

def GetAllCandidates():
    connection = dao.OpenConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM candidates")
    for row in cursor:
        print("Row: ", row)

    connection.close()

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