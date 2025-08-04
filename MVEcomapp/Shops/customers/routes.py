from flask import Blueprint, render_template, request, url_for, flash, redirect
from Shops.models import Product, Category, User
from Shops.extensions import db # You might not need this here, but it's good practice

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/')
@customer_bp.route('/home')
def home():
    featured_products = Product.query.order_by(Product.views_count.desc()).limit(8).all()
    latest_products = Product.query.order_by(Product.timestamp.desc()).limit(8).all()
    categories = Category.query.all()
    return render_template('customer/home.html',
                           featured_products=featured_products,
                           latest_products=latest_products,
                           categories=categories)
                           
@customer_bp.route('/search_results')
def search_results():
    query = request.args.get('query')
    products_query = Product.query.filter(Product.name.ilike(f'%{query}%'))
    products = products_query.all()
    categories = Category.query.all()
    
    return render_template('customer/search_results.html',
                           products=products,
                           query=query,
                           categories=categories)

# You will need to add more routes for the other pages
