from flask import Flask
from routes.dashboard import bp as dashboard
from routes.scanned_activity import bp as scanned_activity
from routes.detected_malware import bp as detected_malware
from routes.reports import bp as reports
from routes.settings import bp as settings
from routes.quarantine import bp as quarantine

app = Flask(__name__)


app.register_blueprint(dashboard)
app.register_blueprint(scanned_activity)
app.register_blueprint(detected_malware)
app.register_blueprint(reports)
app.register_blueprint(settings)
app.register_blueprint(quarantine)


if __name__ == '__main__':
    app.run(debug=True)
