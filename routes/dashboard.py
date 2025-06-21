from flask import Blueprint, render_template

bp = Blueprint('dashboard',__name__, template_folder='templates')

@bp.route('/')
def dashboard():
    return render_template('dashboard.html')
