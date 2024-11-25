# GitHub Repositories Viewer

A simple web application built using Flask that allows users to view their GitHub repositories by entering their GitHub username. The app fetches repository details using the GitHub API and displays them dynamically.

## Features
- Fetches a list of repositories for a given GitHub username.
- Displays repository name, description, language, and stargazer count.
- Stores repository details in a database if they are not already saved.
- Handles errors such as invalid usernames or API failures gracefully.

## Technologies Used
- **Python**: The core programming language.
- **Flask**: For building the web application.
- **SQLAlchemy**: For database integration.
- **GitHub API**: To fetch repository details.
- **Jinja2**: For dynamic rendering of HTML templates.

## Prerequisites
- Python 3.7+
- Flask
- SQLAlchemy
- GitHub Personal Access Token (to access private/public repositories)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/github-repos-viewer.git
   cd github-repos-viewer


Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the application:

Create a config.py file in the root directory with the following content:
python
Copy code
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # Change if using a different database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GITHUB_TOKEN = 'your_github_personal_access_token'
Replace your_github_personal_access_token with your GitHub personal access token.
Initialize the database:

bash
Copy code
flask db upgrade
Run the application:

bash
Copy code
flask run
Open your browser and go to http://127.0.0.1:5000.

Usage
Enter a GitHub username in the text box.
Click "Get Repos" to fetch and display the repositories.
View repository details such as name, description, language, and stargazers.

Known Issues
API rate limits may affect frequent usage without authentication.
Handling very large repository data sets could slow down the app.
Future Enhancements
Add user authentication for personalized features.
Display repository statistics (forks, watchers, etc.).
Support for pagination and improved UI.