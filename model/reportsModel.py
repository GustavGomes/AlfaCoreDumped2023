# Classe para representar a tabela de relatórios 
class Reports:
    # Construtor da classe
    def __init__(self, Id='', ReporterName='', CostCenter='', Description='', OperationField='', CreatedAt='1970-01-01', Location='', images=[]):
        self.Id = Id
        self.ReporterName = ReporterName
        self.CostCenter = CostCenter
        self.Description = Description
        self.OperationField = OperationField
        self.CreatedAt = CreatedAt
        self.Location = Location
        self.images = images
        if(len(images) == 0):
            self.images = ['', '', '']

    # Retorna um dicionário com os dados da classe para facilitar a conversão para JSON
    def __dict__(self) -> dict:
        return {
            'Id': self.Id,
            'ReporterName': self.ReporterName,
            'CostCenter': self.CostCenter,
            'Description': self.Description,
            'OperationField': self.OperationField,
            'CreatedAt': self.CreatedAt,
            'Location': self.Location,
            'images': self.images
        }
    
    