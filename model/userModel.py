# Classe para representar a tabela de usuários
class User:
    # Construtor da classe
    def __init__(self,Id='', Username='', Password='', Cpf='', Gender='', RoleName='', RoleId='', Cbo='', Permission=''):
        self.Id = Id
        self.Username = Username
        self.Password = Password
        self.Cpf = Cpf
        self.Gender = Gender
        self.RoleName = RoleName
        self.RoleId = RoleId
        self.Cbo = Cbo
        self.Permission = Permission
    

    # Retorna um dicionário com os dados da classe para facilitar a conversão para JSON
    def __dict__(self) -> dict:
        return {
            'Id': self.Id,
            'Username': self.Username,
            'Password': self.Password,
            'Cpf': self.Cpf,
            'Gender': self.Gender,
            'RoleName': self.RoleName,
            'RoleId': self.RoleId,
            'Cbo': self.Cbo,
            'Permission': self.Permission
        }
        