# from flask import render_template, redirect, url_for
# from app.controllers.datarecord import DataRecord

# class Application():

#     def __init__(self):
#         self.pages = {
#             'pagina': self.pagina
#         }
#         self.models = DataRecord()

#     def render(self, page, parameter=None):
#         content = self.pages.get(page, self.helper)
#         if not parameter:
#             return content()
#         else:
#             return content(parameter)

#     def helper(self):
#         # Retorna o template 'helper' com Flask
#         return render_template('helper.html')

#     def pagina(self, parameter=None):
#         if not parameter:
#             # Passa a variável 'transfered' e 'data' para o template
#             return render_template('pagina.html', transfered=False, data={})
#         else:
#             # Chama o método do model e obtém dados com o parâmetro
#             info = self.models.work_with_parameter(parameter)
#             if not info:
#                 # Redireciona para a página '/pagina' se não encontrar informações
#                 return redirect(url_for('action_pagina'))
#             else:
#                 # Passa os dados obtidos para o template 'pagina'
#                 return render_template('pagina.html', transfered=True, data=info)