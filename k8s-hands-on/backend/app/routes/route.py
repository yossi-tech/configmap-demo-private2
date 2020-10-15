from flask import request, Blueprint,jsonify
from datetime import datetime
import os

RouteExample = Blueprint('RouteExample', __name__, template_folder='routes')

@RouteExample.route('/', methods=['GET'])
def get():
    host = os.getenv('HOSTNAME')
    current_time = datetime.now().strftime("%H:%M:%S")
    return jsonify(
        {'mesagge':f'Hello World, TIME : {current_time}, HOST: {host} '}
    )
