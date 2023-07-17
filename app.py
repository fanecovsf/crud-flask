from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from models.models import db, Estudante

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'



@app.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return render_template('index.html', estudantes=estudantes)


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        estudante = Estudante(request.form['nome'], request.form['idade'])
        db.session.add(estudante)
        db.session.commit()
        return redirect(url_for('index'))
    
    else:
        return render_template('add.html')
    

@app.route('/delete/<int:id>')
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    if request.method == 'POST':
        estudante.nome = request.form['nome']
        estudante.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit.html', estudante=estudante)


if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)