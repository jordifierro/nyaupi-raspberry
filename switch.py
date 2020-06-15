import os
from flask import Flask, request, jsonify
from storage import set_alarm_active, status
app = Flask(__name__)

@app.route('/on', methods=['POST'])
def activate_alarm():
    if correct_auth_token(request):
        set_alarm_active(True)
        return status()
    else:
        return jsonify({'error':'Unauthorized'}), 404

@app.route('/off', methods=['POST'])
def deactivate_alarm():
    if correct_auth_token(request):
        set_alarm_active(False)
        return status()
    else:
        return jsonify({'error':'Unauthorized'}), 404

def correct_auth_token(request):
    return request.headers['Authorization'].replace('Token ', '') == os.environ['SECRET_KEY']
