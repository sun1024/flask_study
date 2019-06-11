from flask import Flask, abort, redirect, url_for

# 重定向和错误
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)