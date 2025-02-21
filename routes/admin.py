from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.controllers.database.db import users
from app.models.user_model import UserAccount
from app.exceptions import UserAlreadyExistsException, AdminUserNotAllowedException

admin_bp = Blueprint('admin', __name__, template_folder='app/views/html', static_folder='app/static')

@admin_bp.route('/')
def lista_usuarios():
    """ listar os clientes """
    return render_template('lista_usuarios.html', users=users)


@admin_bp.route('/inserir', methods=['POST'])
def inserir_usuario():
    try:
        data = request.json
        
    
        
        # Verifica se o usuário já existe
        for user in users:
            if user["username"] == data['nome']:
                raise UserAlreadyExistsException("Usuário já existe.")
       
        # Verifica se o usuário é um administrador
        if data['nome'].lower() == "admin" or data['nome'].lower() == "admin2":
            raise AdminUserNotAllowedException("Usuário administrador não é permitido.")
        
        # Cria e salva o novo usuário
        new_user = UserAccount(None, data['nome'], data['senha'])
        new_user.save()
        
        return render_template('item_usuario.html', user=new_user)
        
       
        
    
    except UserAlreadyExistsException as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 400
    
    except AdminUserNotAllowedException as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 400

@admin_bp.route('/new')
def form_usuario():
    """ formulario para cadastrar um cliente """
    return render_template('form_usuario.html')


@admin_bp.route('/<int:user_id>/delete', methods=['DELETE'])
def deletar_usuario(user_id):
    global users
    # Remove o usuário com o ID especificado
    users = [user for user in users if user['id'] != user_id]
    
    # Reindexa os IDs dos usuários restantes
    for index, user in enumerate(users):
        user['id'] = index + 1
    
    return '', 204


@admin_bp.route('/<int:user_id>')
def detalhe_usuario(user_id):
    """ exibir detalhes do cliente """
    
    user = list(filter(lambda u: u['id'] == user_id, users))[0]
    return render_template('detalhe_usuario.html', user=user)
    

@admin_bp.route('/<int:user_id>/edit')
def form_edit_usuario(user_id):
    """ formulario para editar um user """
    user = None 
    for u in users:
        if u["id"] == user_id:
            user = u
    
    return render_template('form_usuario.html', user=user)

@admin_bp.route('/<int:user_id>/update', methods=['PUT'])
def atualizar_usuario(user_id):
    """ atualizar informacoes do cliente """
    user_editado = None
    # obter dados do formulario de edicao
    data = request.json
    
    # obter usuario pelo id
    for u in users:
        if u['id'] == user_id:
            u['username'] = data['nome']
            u['password'] = data['senha']
            
            user_editado = u
            
    # editar usuario
    return render_template('item_usuario.html', user=user_editado)
    