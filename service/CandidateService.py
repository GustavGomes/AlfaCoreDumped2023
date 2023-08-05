from flask import jsonify, Request, Response
from dao import candidateDao
from model.candidatesModel import Candidate

# Insere um novo candidato no banco de dados com os dados vindos do front-end
# Campos de arquivo estão como path, não como arquivo
def InsertCandidate(request) -> Response:
    c = Candidate(id=request.json['id'], CandidateName=request.json['candidateName'], MotherName=request.json['motherName'], FatherName=request.json['fatherName'], Gender=request.json['gender'], CiviState=request.json['civiState'], EducationLevel=request.json['educationLevel'], Ethnicity=request.json['ethnicity'], BirthDate=request.json['birthDate'],
                 Nacionality=request.json['nacionality'], BirthCountry=request.json['birthCountry'], BirthState=request.json['birthState'], BirthCity=request.json['birthCity'], ShoeSize=request.json['shoeSize'], PantsSize=request.json['pantsSize'], ShirtSize=request.json['shirtSize'], TelephoneNumber=request.json['telephoneNumber'],
                 SecondTelephoneNumber=request.json['secondTelephoneNumber'], Email=request.json['email'], Cep=request.json['cep'], Country=request.json['country'], State=request.json['state'], City=request.json['city'], Neighborhood=request.json['neighborhood'], ResidencyType=request.json['residencyType'], Street=request.json['street'], ResidencyNumber=request.json['residencyNumber'], Complement=request.json['complement'],
                 RgNumber=request.json['rgNumber'], RgEmissorCity=request.json['rgEmissorCity'], RgReleaseDate=request.json['rgReleaseDate'], Cpf=request.json['cpf'], Pispasep=request.json['pispasep'], Function=request.json['function'], Lodged=request.json['lodged'],
                 Pcd=request.json['pcd'], RgFile=request.json['rgFile'], CpfFile=request.json['cpfFile'], ResumeFile=request.json['resumeFile'], CnhFile=request.json['cnhFile'], ArmyFile=request.json['armyFile'], HasFriendFamiliar=request.json['hasFriendFamiliar'])
    return candidateDao.InsertCandidate(c)

def GetCandidates() -> Response:
    candidates = candidateDao.GetCandidates()
    candidates_list = [candidate._dict_() for candidate in candidates]
    return jsonify(candidates_list)

def GetCandidateById(request) -> Response:
    id = request.args.get('id')
    return jsonify(candidateDao.GetCandidateById(id)._dict_())