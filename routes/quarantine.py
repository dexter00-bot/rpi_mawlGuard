from flask import Blueprint, render_template

bp = Blueprint('quarantine',__name__, template_folder='templates')

@bp.route('/quarantine')
def quarantine():
    return render_template('quarantine.html')
