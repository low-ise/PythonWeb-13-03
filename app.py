from flask import Flask, render_template

app = Flask('Hello')

@app.route('/')
@app.route('/teste')
def hello():
    return "Hello world, buenos días, muchachosssss"

@app.route('/cat')
def alunos():
    return render_template('hello.html')