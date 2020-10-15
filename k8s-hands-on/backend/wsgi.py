from app.app import create_app
import os
from werkzeug.middleware.proxy_fix import ProxyFix
# do some production specific things to the app

env = os.getenv('ENV','development') 
app = create_app(env)
# app.wsgi_app = ProxyFix(app.wsgi_app)
    