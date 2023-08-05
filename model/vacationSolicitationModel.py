class VacationSolicitation:
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