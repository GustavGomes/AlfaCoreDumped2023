# Classe para representar a tabela de candidatos
class Candidate:
    # Construtor da classe
    def __init__(self, id, CandidateName, MotherName, FatherName, Gender, CiviState, EducationLevel, Ethnicity, BirthDate,
                 Nacionality, BirthCountry, BirthState, BirthCity, ShoeSize, PantsSize, ShirtSize, TelephoneNumber,
                 SecondTelephoneNumber, Email, Cep, Country, State, City, Neighborhood, ResidencyType, Street, ResidencyNumber, Complement,
                 RgNumber, RgEmissorCity, RgReleaseDate, Cpf, Pispasep, Function, Lodged,
                 Pcd, RgFile, CpfFile, ResumeFile, CnhFile, ArmyFile, HasFriendFamiliar):
        self.id = id
        self.CandidateName = CandidateName
        self.MotherName = MotherName
        self.FatherName = FatherName
        self.Gender = Gender
        self.CiviState = CiviState
        self.EducationLevel = EducationLevel
        self.Ethnicity = Ethnicity
        self.BirthDate = BirthDate
        self.Nacionality = Nacionality
        self.BirthCountry = BirthCountry
        self.BirthState = BirthState
        self.BirthCity = BirthCity
        self.ShoeSize = ShoeSize
        self.PantsSize = PantsSize
        self.ShirtSize = ShirtSize
        self.TelephoneNumber = TelephoneNumber
        self.SecondTelephoneNumber = SecondTelephoneNumber
        self.Email = Email
        self.Cep = Cep
        self.Country = Country
        self.State = State
        self.City = City
        self.Neighborhood = Neighborhood
        self.ResidencyType = ResidencyType
        self.Street = Street
        self.ResidencyNumber = ResidencyNumber
        self.Complement = Complement
        self.RgNumber = RgNumber
        self.RgEmissorCity = RgEmissorCity
        self.RgReleaseDate = RgReleaseDate
        self.Cpf = Cpf
        self.Pispasep = Pispasep
        self.Function = Function
        self.Lodged = Lodged
        self.Pcd = Pcd
        self.RgFile = RgFile
        self.CpfFile = CpfFile
        self.ResumeFile = ResumeFile
        self.CnhFile = CnhFile
        self.ArmyFile = ArmyFile
        self.HasFriendFamiliar = HasFriendFamiliar
    
    # Retorna um dicionário com os dados da classe para facilitar a conversão para JSON
    def _dict_(self) -> dict:
        return {
            'id': self.id,
            'CandidateName': self.CandidateName,
            'MotherName': self.MotherName,
            'FatherName': self.FatherName,
            'Gender': self.Gender,
            'CiviState': self.CiviState,
            'EducationLevel': self.EducationLevel,
            'Ethnicity': self.Ethnicity,
            'BirthDate': self.BirthDate,
            'Nacionality': self.Nacionality,
            'BirthCountry': self.BirthCountry,
            'BirthState': self.BirthState,
            'BirthCity': self.BirthCity,
            'ShoeSize': self.ShoeSize,
            'PantsSize': self.PantsSize,
            'ShirtSize': self.ShirtSize,
            'TelephoneNumber': self.TelephoneNumber,
            'SecondTelephoneNumber': self.SecondTelephoneNumber,
            'Email': self.Email,
            'Cep': self.Cep,
            'Country': self.Country,
            'State': self.State,
            'City': self.City,
            'Neighborhood': self.Neighborhood,
            'ResidencyType': self.ResidencyType,
            'Street': self.Street,
            'ResidencyNumber': self.ResidencyNumber,
            'Complement': self.Complement,
            'RgNumber': self.RgNumber,
            'RgEmissorCity': self.RgEmissorCity,
            'RgEmissorCity': self.RgEmissorCity,
            'RgReleaseDate': self.RgReleaseDate,
            'Cpf': self.Cpf,
            'Pispasep': self.Pispasep,
            'Function': self.Function,
            'Lodged': self.Lodged,
            'Pcd': self.Pcd,
            'RgFile': self.RgFile,
            'CpfFile': self.CpfFile,
            'ResumeFile': self.ResumeFile,
            'CnhFile': self.CnhFile,
            'ArmyFile': self.ArmyFile,
            'HasFriendFamiliar': self.HasFriendFamiliar
        }