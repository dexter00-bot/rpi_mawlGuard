from flask import Blueprint, render_template

bp = Blueprint('scanned_activity',__name__, template_folder='templates')

@bp.route('/scanned_activity')
def scanned_activity():
    return render_template('scanned_activity.html')
