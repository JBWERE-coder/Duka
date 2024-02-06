# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Change this based on your chosen database
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
