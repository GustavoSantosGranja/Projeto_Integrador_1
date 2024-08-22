# Api -> lugar para disponibilizar recursos e funcionalidades. Uma ponte
# 1 Objetivo -  cria uma API que disponibiliza a consulta, criação, edição e exclusão de carros
# 2 URL Base - localhost
# 3 Endpoints -
    #localhost/carros(GET)
    #localhost/carros(PUT)
    #localhost/carros(DELETE)
    #localhost/carros id (GET)

from flask import Flask
#importa o banco de dados 
from bd import Carros

#instanciar o módulo flask na variavel app
app = Flask('carros')

#primeiro método - Visualizar dados (get)
@app.route('/carros' methods=['GET'])

#primeiro método parte  - visualizar dados por ID (get/id)

#Segundo método - criar novos dados (post)

#Terceiro método -  editar dados (put)

#Quarto método -  deletar dados (delete)