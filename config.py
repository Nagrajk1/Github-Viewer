import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

print(os.getenv('DATABASE_URL'))

# Load environment variables from .env file
load_dotenv()

# Configuration class
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Ensure DATABASE_URL is correct in .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Create Flask app
app = Flask(__name__)

# Load configuration into Flask app
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Example model (optional, to test database connection)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Example route to verify app is running
@app.route('/')
def home():
    return "Hello, Flask with SQLAlchemy is working!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
os.environ["DATABASE_URL"] = "mysql+pymysql://root:Root123@localhost:3306/github"

print(os.getenv('DATABASE_URL'))
