from flask import Flask
from flask_session import Session
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # In production, use environment variable

# Configure Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Import routes after app initialization to avoid circular imports
from routes import *
