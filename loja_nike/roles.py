from rolepermissions.roles import AbstractUserRole

class Adminstrador(AbstractUserRole):
    available_permissions = {'admin':True}

