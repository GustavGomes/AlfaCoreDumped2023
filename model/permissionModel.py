# Classe para representar a tabela de permissões de um usuário
class Permission:
    # Construtor da classe
    def __init__(self, Id='', PermissionName='', UserID=''):
        self.Id = Id
        self.PermissionName = PermissionName
        self.UserID = UserID
    # Retorna um dicionário com os dados da classe para facilitar a conversão para JSON
    def __dict__(self) -> dict:
        return {
            'id': self.Id,
            'PermissionName': self.PermissionName,
            'UserID': self.UserID,
        }