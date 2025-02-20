# filepath: /home/felipe-pedroza/Documentos/Felipe/python/projeto_final-OO/bmvc_start_from_this-main/route.py
from flask import Flask, render_template, request, send_from_directory,redirect, url_for
from flask_socketio import SocketIO
#from app.controllers.application import Application
from routes.user import user_bp, register_socketio_events
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.home import home_bp


app = Flask(__name__, static_folder='app/static', template_folder='app/views/html')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#ctl = Application()

#-----------------------------------------------------------------------------
# Rotas:

@app.route('/', methods=['GET'])
def root():
    return redirect(url_for('auth.login'))

# Registrando os Blueprint 
app.register_blueprint(home_bp, url_prefix='/adm')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(admin_bp, url_prefix='/admin')


# Servindo arquivos estáticos (css, js, imagens)
@app.route('/static/<path:filepath>')
def serve_static(filepath):
    return send_from_directory('app/static', filepath)

# Rota para a página principal
@app.route('/pagina', methods=['GET'])
def pagina():
    return render_template('pagina.html')


# Rota para a página de teste do WebSocket
@app.route('/socket', methods=['GET'])
def socket_test():
    return render_template('socket_test.html')

#-----------------------------------------------------------------------------
# Outras rotas adicionais aqui

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Eventos WebSocket:

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('response', {'message': 'Connected to WebSocket'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

#-----------------------------------------------------------------------------


# Registrar eventos do SocketIO
register_socketio_events(socketio)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080, debug=True)