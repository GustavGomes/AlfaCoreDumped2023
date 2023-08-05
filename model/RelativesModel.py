class Relatives:
    def __init__(self, Id='', CandidateId='', Cpf='', Name='', Kinship='', Birthday=''):
        self.Id = Id
        self.CandidateId = CandidateId
        self.Cpf = Cpf
        self.Name = Name
        self.Kinship = Kinship
        self.Birthday = Birthday

    def __dict__(self) -> dict:
        return {
            'Id': self.Id,
            'CandidateId': self.CandidateId,
            'Cpf': self.Cpf,
            'Name': self.Name,
            'Kinship': self.Kinship,
            'Birthday': self.Birthday,
        }
