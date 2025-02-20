# filepath: /home/felipe-pedroza/Documentos/Felipe/python/projeto_final-OO/bmvc_start_from_this-main/routes/user.py
from flask import Blueprint, render_template
from flask_socketio import emit

user_bp = Blueprint('user_bp', __name__, template_folder='app/views/html')

@user_bp.route('/')
def root():
    return render_template('pagina.html')


def register_socketio_events(socketio):
    @socketio.on('message')
    def handle_message(message):
        print('received message: ' + message)
        socketio.emit('response', {'data': 'Message received!'})

