from flask import jsonify, Request, Response
from dao import candidateDao
from model.candidatesModel import Candidate
import datetime
import Utils

# Insere um novo candidato no banco de dados com os dados vindos do front-end
# Campos de arquivo estão como path, não como arquivo
def InsertCandidate(request) -> Response:
    # Cria um objeto do tipo Candidate com os dados do body request
    c = Candidate(id=0, CandidateName=request.json['name'], MotherName=request.json['mother_name'], FatherName=request.json['father_Name'], Gender=request.json['genre'], CiviState=request.json['civil_state'], EducationLevel=request.json['education_level'], Ethnicity=request.json['ethnicity'], BirthDate=request.json['birth_Date'],
                 Nacionality=request.json['nacionality'], BirthCountry=request.json['birth_country'], BirthState=request.json['birth_state'], BirthCity=request.json['birth_city'], ShoeSize=request.json['shoe_size'], PantsSize=request.json['pants_size'], ShirtSize=request.json['shirt_size'], TelephoneNumber=request.json['telephone_number'],
                 SecondTelephoneNumber=request.json['second_telephone_number'], Email=request.json['email'], Cep=request.json['cep'], Country=request.json['country'], State=request.json['state'], City=request.json['city'], Neighborhood=request.json['neighborhood'], ResidencyType=request.json['residency_type'], Street=request.json['street'], ResidencyNumber=request.json['residency_number'], Complement=request.json['complement'],
                 RgNumber=request.json['rg_number'], RgEmissorCity=request.json['rg_emissor_city'], RgReleaseDate=request.json['rg_release_date'], Cpf=request.json['cpf'], Pispasep=request.json['pispasep'], Function=request.json['function'], Lodged=request.json['lodged'],
                 Pcd=request.json['pcd'], ArmyFile=request.json['cnh_file'], HasFriendFamiliar=request.json['has_friend_familiar'],RgFile='', CpfFile='', ResumeFile='', CnhFile='')
    # Corrije o tamanho dos campos para não dar erro no banco de dados com o timestamp
    c.BirthDate = c.BirthDate[0:10]
    c.BirthCity = c.BirthCity[0:10]
    c.BirthState = c.BirthState[0:10]
    c.BirthCountry = c.BirthCountry[0:10]

    Utils.sendZapMessage("Olá, " + c.CandidateName + "! Seu cadastro foi realizado com sucesso! Aguarde o contato de um de nossos recrutadores.", c.TelephoneNumber)
    # Chama a função da DAO que insere o candidato no banco de dados
    return candidateDao.InsertCandidate(c)

# Atualiza um candidato no banco de dados com os dados vindos do front-end
def GetCandidates() -> Response:
    # Chama a função da DAO que recupera os candidatos no banco de dados
    candidates = candidateDao.GetCandidates()
    # Converte os candidatos para uma lista de dicionários para facilitar a conversão para JSON
    candidates_list = [candidate._dict_() for candidate in candidates]
    # Retorna a lista de candidatos em formato JSON
    return jsonify(candidates_list)

# Atualiza um candidato no banco de dados com os dados vindos do front-end
def GetCandidateById(request) -> Response:
    # Recupera o id do candidato nos argumentos da request
    id = request.args.get('id')
    # Chama a função da DAO que recupera o candidato no banco de dados
    return jsonify(candidateDao.GetCandidateById(id)._dict_())