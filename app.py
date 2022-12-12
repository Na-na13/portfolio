import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def get_repos():
    api_url = "https://api.github.com/users/Na-na13/repos"
    response = requests.get(api_url).json()
    repos = []
    for data in response:
        if 'ohtu' not in data['name']:
            repo = {}
            repo['name'] = data['name'].replace("-", " ")
            repo['description'] = data['description']
            repo['language'] = data['language']
            repo['topics'] = data['topics']
            repo['html_url'] = data['html_url']
            repo['updated_at'] = data['updated_at']
            repos.append(repo)
    return render_template("projects.html", repos=repos)
