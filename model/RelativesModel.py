# Classe para representar a tabela de dependentes de um candidato
class Relatives:
    # Construtor da classe
    def __init__(self, Id='', CandidateId='', Cpf='', Name='', Kinship='', Birthday=''):
        self.Id = Id
        self.CandidateId = CandidateId
        self.Cpf = Cpf
        self.Name = Name
        self.Kinship = Kinship
        self.Birthday = Birthday

    # Retorna um dicionário com os dados da classe para facilitar a conversão para JSON
    def __dict__(self) -> dict:
        return {
            'Id': self.Id,
            'CandidateId': self.CandidateId,
            'Cpf': self.Cpf,
            'Name': self.Name,
            'Kinship': self.Kinship,
            'Birthday': self.Birthday,
        }
