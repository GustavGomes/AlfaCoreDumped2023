class Equipment:
    def __init__(self, Id='', Code='', Description='', LiberationStatus='', PdfFile=''):
        self.Id = Id
        self.Code = Code
        self.Description = Description
        self.LiberationStatus = LiberationStatus
        self.PdfFile = PdfFile
        
    def __dict__(self) -> dict:
        return {
            'Id':self.Id,
            'Code':self.Code,
            'Description':self.Description,
            'LiberationStatus':self.LiberationStatus,
            'PdfFile':self.PdfFile,
        }