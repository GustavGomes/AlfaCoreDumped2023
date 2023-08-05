class Permission:
    def __init__(self, Id='', PermissionName='', UserID=''):
        self.Id = Id
        self.PermissionName = PermissionName
        self.UserID = UserID

    def __dict__(self) -> dict:
        return {
            'id': self.Id,
            'PermissionName': self.PermissionName,
            'UserID': self.UserID,
        }