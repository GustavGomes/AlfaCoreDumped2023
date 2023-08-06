# Classe para representar a tabela de solicitação de férias
class VacationSolicitation:
    # Construtor da classe
    def __init__(self, id, CreatorId, TargetId, Status, VacationStart, VacationEnd, Description, CreationDate, StartDate,
                 EndDate, UserId):
        
        self.id = id
        self.CreatorId = CreatorId
        self.TargetId = TargetId
        self.Status = Status
        self.VacationStart = VacationStart
        self.VacationEnd = VacationEnd
        self.Description = Description
        self.CreationDate = CreationDate
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.UserId = UserId

    # Retorna um dicionário com os dados da classe para facilitar a conversão para JSON
    def _dict_(self) -> dict:
        return {
            'id': self.id,
            'CreatorId': self.CreatorId,
            'TargetId': self.TargetId,
            'Status': self.Status,
            'VacationStart': self.VacationStart,
            'VacationEnd': self.VacationEnd,
            'Description': self.Description,
            'CreationDate': self.CreationDate,
            'StartDate': self.StartDate,
            'EndDate': self.EndDate,
            'UserId': self.UserId
        }