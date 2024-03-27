from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = "banco.bd"
SECRET_KEY = "1234"
app.config.from_object(__name__)

@app.before_request
def before_request():
    g.bd = sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(p):
    if hasattr(g, 'bd'):
        g.bd.close()

@app.route('/')
def ola():
    user_name = "Lou"
    user_list = ["Lorena", "Daniel", "Danielle", "Luana"]
    posts = [{"title": "My title", "text": "My text", "creation_date": "03.27.24"},
             {"title": "My title2", "text": "My text2", "creation_date": "03.23.24"}]
    return render_template("hello.html", post=posts)