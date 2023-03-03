import os
import dotenv 

dotenv.load_dotenv()

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')

MONGODB_SETTINGS = {
    'db': os.getenv('MONGO_DBNAME'),
    'host': os.getenv('MONGO_URI'),
    'port': 27017
}

# Configurações do Flask-Security
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False

MONGO_URI = os.getenv('MONGO_URI')
