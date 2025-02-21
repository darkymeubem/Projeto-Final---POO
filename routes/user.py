from flask import Blueprint, render_template, session, redirect, url_for
from app.models.user_model import UserAccount

user_bp = Blueprint('user_bp', __name__, template_folder='app/views/html')

@user_bp.route('/<int:user_id>')
def root(user_id):
    # Verifica se o usuário está logado
    if 'user_id' in session and session['user_id'] == user_id:
        # Busca o usuário pelo ID
        user = UserAccount.get_by_id(user_id)
        
        if user:
            return render_template('pagina.html', user=user)  # Passa o objeto user para o template
        else:
            return "Usuário não encontrado.", 404
    else:
        return redirect(url_for('auth.login'))  # Redireciona para o login se o usuário não estiver autenticado
    
    
def register_socketio_events(socketio):
    @socketio.on('message')
    def handle_message(message):
        print('received message: ' + message)
        socketio.emit('response', {'data': 'Message received!'})

