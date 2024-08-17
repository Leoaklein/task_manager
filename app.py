# Importa a classe Flask do pacote flask
from flask import Flask

# Importa a instância de SQLAlchemy 'db' e o blueprint 'main' dos módulos 'models' e 'routes'
from models import db
from routes import main

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Configura a URI do banco de dados para usar um banco de dados SQLite chamado 'tasks.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

# Desativa o rastreamento de modificações do SQLAlchemy para economizar recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a instância do SQLAlchemy com a aplicação Flask
db.init_app(app)

# Registra o blueprint 'main' na aplicação Flask, adicionando suas rotas e funcionalidades
app.register_blueprint(main)

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Cria um contexto de aplicação para executar operações que dependem da configuração do app
    with app.app_context():
        # Cria todas as tabelas do banco de dados definidas nos modelos SQLAlchemy
        db.create_all()
    # Inicia o servidor de desenvolvimento Flask com o modo de depuração ativado
    app.run(debug=True)
