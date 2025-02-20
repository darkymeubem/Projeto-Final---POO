from app.controllers.database.db import admins
from app.models.user_model import UserAccount

class AdminAccount(UserAccount):
    def __init__(self, id, username, password):
        super().__init__(id, username, password)
        self.admin = True

    @staticmethod
    def authenticate(username, password):
        for admin in admins:
            if admin["username"] == username and admin["password"] == password:
                return AdminAccount(admin["id"], admin["username"], admin["password"])
        return None
    
    