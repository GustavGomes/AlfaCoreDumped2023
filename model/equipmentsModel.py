# Classe representando a tabela Equipamentos do banco de dados
class Equipment:
    # Construtor da classe
    def __init__(self, Id='', Code='', Description='', LiberationStatus='', PdfFile=''):
        self.Id = Id
        self.Code = Code
        self.Description = Description
        self.LiberationStatus = LiberationStatus
        self.PdfFile = PdfFile
        
    # Retorna um dicionário com os dados da classe para facilitar a conversão para JSON
    def __dict__(self) -> dict:
        return {
            'Id':self.Id,
            'Code':self.Code,
            'Description':self.Description,
            'LiberationStatus':self.LiberationStatus,
            'PdfFile':self.PdfFile,
        }