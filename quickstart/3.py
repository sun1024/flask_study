from flask import Flask, request, url_for

# HTTP 方法
app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else :
#         return show_the_login_form()

url_for('static', filename='style.css')