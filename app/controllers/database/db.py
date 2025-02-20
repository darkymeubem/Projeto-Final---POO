# Dados de usuários
users = [
    {"id": 1, "username": "user1", "password": "password1"},
    {"id": 2, "username": "user2", "password": "password2"}
]

def add_user(user):
    user["id"] = len(users) + 1
    users.append(user)



# Dados de administradores
admins = [
    {"id": 1, "username": "admin", "password": "admin"},
    {"id": 2, "username": "admin2", "password": "admin2"}
]

# Função para obter um usuário pelo nome de usuário
def get_user_by_username(username):
    for user in users:
        if user["username"] == username:
            return user
    return None

# Função para obter um administrador pelo nome de usuário
def get_admin_by_username(username):
    for admin in admins:
        if admin["username"] == username:
            return admin
    return None