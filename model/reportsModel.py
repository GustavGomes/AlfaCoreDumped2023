class Reports:
    def __init__(self, Id='', ReporterName='', CostCenter='', Description='', OperationField='', CreatedAt='', Location=''):
        self.Id = Id
        self.ReporterName = ReporterName
        self.CostCenter = CostCenter
        self.Description = Description
        self.OperationField = OperationField
        self.CreatedAt = CreatedAt
        self.Location = Location

    def __dict__(self) -> dict:
        return {
            'Id': self.Id,
            'ReporterName': self.ReporterName,
            'CostCenter': self.CostCenter,
            'Description': self.Description,
            'OperationField': self.OperationField,
            'CreatedAt': self.CreatedAt,
            'Location': self.Location,
        }
    
    