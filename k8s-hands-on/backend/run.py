from app.app import create_app
import os

if __name__ == '__main__':
    env = os.getenv('ENV','development') 
    app = create_app(env)
    
    app.run(host='0.0.0.0',port=5000)