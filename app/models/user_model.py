from app.controllers.database.db import users, add_user


class UserAccount:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def authenticate(username, password):
        for user in users:
            if user["username"] == username and user["password"] == password:
                return UserAccount(user["id"], user["username"], user["password"])
        return None

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }


    @staticmethod
    def get_by_id(user_id):
        # Simulação de busca por ID (substitua pela lógica real)
        for user in users:
            if user['id'] == user_id:
                return UserAccount(user['id'], user['username'], user['password'])
        return None
    
    def save(self):
        user_data = self.serialize()
        add_user(user_data)
        self.id = user_data["id"]
    
    def delete(self):
        global users
        users = [user for user in users if user["id"] != self.id]
        return {'deleted': 'ok'}