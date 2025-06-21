from flask import Blueprint, render_template

bp = Blueprint('settings',__name__, template_folder='templates')

@bp.route('/settings')
def settings():
    return render_template('settings.html')
