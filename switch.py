from flask import Flask
from storage import set_alarm_active
app = Flask(__name__)

@app.route('/lock')
def activate_alarm():
    set_alarm_active(True)
    return 'Activated!'

@app.route('/unlock')
def deactivate_alarm():
    set_alarm_active(False)
    return 'Deactivated!'
