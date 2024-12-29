from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def dashboard():
    return render_template('admin.html')

# Additional routes for managing blog posts can be added here.