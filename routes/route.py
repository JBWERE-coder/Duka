# routes.py
from flask import render_template
from app import app
from models import Product

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

