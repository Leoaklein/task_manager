# Importa as funções e classes necessárias do Flask e do módulo de modelos
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Task

# Cria um blueprint chamado 'main'. Blueprints ajudam a organizar o código em módulos.
main = Blueprint('main', __name__)

# Define a rota principal ('/') para o blueprint 'main'
@main.route('/')
def index():
    # Consulta todas as tarefas no banco de dados
    tasks = Task.query.all()
    # Renderiza o template 'index.html' e passa a lista de tarefas para ele
    return render_template('index.html', tasks=tasks)

# Define a rota '/add' para adicionar uma nova tarefa, aceita apenas requisições POST
@main.route('/add', methods=['POST'])
def add_task():
    # Obtém o valor do campo 'title' enviado pelo formulário HTML
    title = request.form.get('title')
    # Cria uma nova instância do modelo 'Task' com o título fornecido
    new_task = Task(title=title)
    # Adiciona a nova tarefa à sessão do banco de dados
    db.session.add(new_task)
    # Confirma a transação, salvando a nova tarefa no banco de dados
    db.session.commit()
    # Redireciona o usuário de volta para a página principal
    return redirect(url_for('main.index'))

# Define a rota '/update/<int:task_id>' para atualizar o status de uma tarefa
@main.route('/update/<int:task_id>')
def update_task(task_id):
    # Obtém a tarefa com o ID fornecido do banco de dados
    task = Task.query.get(task_id)
    # Alterna o estado da tarefa (se está feita ou não)
    task.done = not task.done
    # Confirma a transação, salvando a alteração no banco de dados
    db.session.commit()
    # Redireciona o usuário de volta para a página principal
    return redirect(url_for('main.index'))

# Define a rota '/delete/<int:task_id>' para deletar uma tarefa
@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    # Obtém a tarefa com o ID fornecido do banco de dados
    task = Task.query.get(task_id)
    # Marca a tarefa para ser deletada do banco de dados
    db.session.delete(task)
    # Confirma a transação, removendo a tarefa do banco de dados
    db.session.commit()
    # Redireciona o usuário de volta para a página principal
    return redirect(url_for('main.index'))
