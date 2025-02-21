from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.user_model import UserAccount
from app.models.admin_model import AdminAccount

auth_bp = Blueprint('auth', __name__, template_folder='app/views/html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtém os dados do formulário
        username = request.form['usuario']
        password = request.form['senha']
        
        # Autentica o usuário
        user = UserAccount.authenticate(username, password)
        admin = AdminAccount.authenticate(username, password)
        
        if user:
            # Armazena o ID do usuário na sessão
            session['user_id'] = user.id
            return redirect(url_for('user_bp.root', user_id=user.id))  # Redireciona para a página do usuário
        elif admin:
            # Armazena o ID do administrador na sessão
            session['admin_id'] = admin.id
            return redirect('/adm')  # Redireciona para a página do admin
        else:
            # Adiciona um novo usuário se não existir
            new_user = UserAccount(None, username, password)
            new_user.save()
            session['user_id'] = new_user.id  # Armazena o ID do novo usuário na sessão
            return redirect(url_for('user_bp.root', user_id=new_user.id))  # Redireciona para a página do novo usuário
    
    # Renderiza o template login.html quando o método for GET
    return render_template('login.html')