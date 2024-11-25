import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from config import Config  # Ensure config.py is properly set up
from models import db, Repository
from services import repo_service  # Ensure repo_service is implemented correctly

# Flask app initialization
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', error=None, repos=None)

@app.route('/repos', methods=['GET'])
def get_repos():
    username = request.args.get('username')
    if not username:
        return render_template('index.html', error="Username is required", repos=None)

    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        'Authorization': f"token {app.config.get('GITHUB_TOKEN', '')}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        repos = response.json()
        for repo in repos:
            existing_repo = repo_service.get_repo_by_repo_and_username(repo['name'], username)
            if not existing_repo:
                new_repo = Repository(
                    name=repo['name'],
                    description=repo.get('description'),
                    language=repo.get('language'),
                    stargazers_count=repo.get('stargazers_count'),
                    username=username
                )
                db.session.add(new_repo)
        db.session.commit()
        return render_template('index.html', repos=repos, error=None)
    except requests.exceptions.RequestException as e:
        return render_template('index.html', error=f"API error: {str(e)}", repos=None)

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
