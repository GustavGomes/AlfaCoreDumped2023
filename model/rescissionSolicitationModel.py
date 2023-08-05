class RescissionSolicitation:
    def __init__(self, id, CreatorId, TargetId, Status, Rank, Reason, Description, CreationDate, StartDate,
                 EndDate, UserId):
        
        self.id = id
        self.CreatorId = CreatorId
        self.TargetId = TargetId
        self.Status = Status
        self.Rank = Rank
        self.Reason = Reason
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
            'Rank': self.Rank,
            'Reason': self.Reason,
            'Description': self.Description,
            'CreationDate': self.CreationDate,
            'StartDate': self.StartDate,
            'EndDate': self.EndDate,
            'UserId': self.UserId
        }