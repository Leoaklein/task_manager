# Importa a classe SQLAlchemy do pacote flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância de SQLAlchemy para gerenciar a conexão e operações com o banco de dados
db = SQLAlchemy()


# Define um modelo de dados chamado 'Task'
class Task(db.Model):
    # Define a coluna 'id' como um inteiro e chave primária
    id = db.Column(db.Integer, primary_key=True)

    # Define a coluna 'title' como uma string com comprimento máximo de 100 caracteres e não permite valores nulos
    title = db.Column(db.String(100), nullable=False)

    # Define a coluna 'description' como uma string com comprimento máximo de 200 caracteres e permite valores nulos
    description = db.Column(db.String(200), nullable=True)

    # Define a coluna 'done' como um booleano com valor padrão False
    done = db.Column(db.Boolean, default=False)

    # Define um metod special para representar a instância do modelo como uma string
    def __repr__(self):
        # Retorna uma string com o título da tarefa, facilitando a visualização durante a depuração
        return f'<Task {self.title}>'
