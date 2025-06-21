from flask import Blueprint, render_template

bp = Blueprint('reports',__name__, template_folder='templates')

@bp.route('/reports')
def reports():
    return render_template('reports.html')
