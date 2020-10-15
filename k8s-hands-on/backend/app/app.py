from flask import Flask, jsonify
from .config.config import config as cfg 
from .routes.route import RouteExample
from flask_cors import CORS

def create_app(env='production'):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(cfg[env])
    app.register_blueprint(RouteExample)
 
    return app