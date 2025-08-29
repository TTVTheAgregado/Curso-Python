#Importação do Flask
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # Configuração do banco de dados SQLite


db = SQLAlchemy(app)  # Inicialização do SQLAlchemy com a aplicação Flask

# Modelagem de exemplo para um produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    descripition = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'

# Definir uma rota para a página inicial e uma função que será executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)  # Executa o servidor Flask em modo de depuração

