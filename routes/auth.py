from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user_model import UserAccount
from app.models.admin_model import AdminAccount

auth_bp = Blueprint('auth', __name__, template_folder='app/views/html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtem os dados do formulario
        username = request.form['usuario']
        password = request.form['senha']
        
        # Autentica o usuário
        user = UserAccount.authenticate(username, password)
        admin = AdminAccount.authenticate(username, password)
        
        if user:
            # Renderiza o template com os dados do usuário
            return redirect('/user')
        elif admin:
            # Renderiza o template com os dados do administrador
            return redirect('/adm') #Pagina CRUD do Admin
        else:
            # Adiciona um novo usuário se não existir
            new_user = UserAccount(None,username, password)
            new_user.save()
            return redirect('/user')
    
    # Renderiza o template login.html quando o método for GET
    return render_template('login.html')