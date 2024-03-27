from flask import Flask, render_template
import sqlite3

app = Flask('Hello')

DATABASE = "banco.bd"
SECRET_KEY = "1234"
app.configure.from_object(__name__)

@app.route('/')

def conect():
    return sqlite3.connect(DATABASE)

def before_request():
    g.bd = connect()

def teardown_request():
    g.bd.close()


def hello():
    return render_template('hello.html')