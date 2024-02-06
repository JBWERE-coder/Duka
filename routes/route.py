# routes.py
from flask import render_template, request, redirect, url_for
from app import app, db
from models import Product, Order, OrderItem

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity', 1))

        product = Product.query.get_or_404(product_id)
        total_price = product.price * quantity

        # Create or get the current order for the user (simplified for demonstration)
        user_id = 1  # Replace with actual user ID
        current_order = Order.query.filter_by(user_id=user_id, completed_at=None).first()

        if not current_order:
            current_order = Order(user_id=user_id)
            db.session.add(current_order)
            db.session.commit()

        order_item = OrderItem(order_id=current_order.id, product_id=product.id, quantity=quantity, total_price=total_price)
        db.session.add(order_item)
        db.session.commit()

        return redirect(url_for('shopping_cart'))

    # GET request: Display current cart items
    user_id = 1  # Replace with actual user ID
    current_order = Order.query.filter_by(user_id=user_id, completed_at=None).first()

    if current_order:
        cart_items = current_order.order_items
    else:
        cart_items = []

    return render_template('shopping_cart.html', cart_items=cart_items)
