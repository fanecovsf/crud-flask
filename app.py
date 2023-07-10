from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

@app.route('/')
def main():
    return '<h1>Online</h1>'

if __name__ == '__main__':
    app.run(debug=True)