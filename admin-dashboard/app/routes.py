from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin_dashboard():
    return render_template('admin/index.html')