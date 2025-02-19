from flask import render_template, request, redirect, url_for, session, flash
from app import app
from models import products, carts
import logging

@app.route('/')
def index():
    search_query = request.args.get('search', '').lower()
    filtered_products = {
        k: v for k, v in products.items()
        if search_query in v['name'].lower() or search_query in v['description'].lower()
    }
    return render_template('index.html', products=filtered_products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = products.get(product_id)
    if not product:
        flash('Product not found', 'error')
        return redirect(url_for('index'))
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    cart_items = carts.get(session.get('cart_id', ''), {})
    total = sum(products[pid]['price'] * qty for pid, qty in cart_items.items())
    cart_products = [(products[pid], qty) for pid, qty in cart_items.items()]
    return render_template('cart.html', cart_items=cart_products, total=total)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart_id' not in session:
        session['cart_id'] = str(hash(str(session)))
    
    if session['cart_id'] not in carts:
        carts[session['cart_id']] = {}
    
    quantity = int(request.form.get('quantity', 1))
    cart = carts[session['cart_id']]
    
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    
    flash('Product added to cart!', 'success')
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Mock checkout process
        cart_id = session.get('cart_id')
        if cart_id in carts:
            del carts[cart_id]
            session.pop('cart_id', None)
            flash('Order completed successfully!', 'success')
            return redirect(url_for('index'))
    return render_template('checkout.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', products=products)

@app.route('/admin/add_product', methods=['POST'])
def add_product():
    new_id = max(products.keys()) + 1 if products else 1
    products[new_id] = {
        'id': new_id,
        'name': request.form['name'],
        'price': float(request.form['price']),
        'description': request.form['description'],
        'image': 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?w=400&h=300&fit=crop',
        'stock': int(request.form['stock'])
    }
    flash('Product added successfully!', 'success')
    return redirect(url_for('admin'))