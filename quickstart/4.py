# from flask import Flask, request
# 文件上传
# app = Flask(__name__)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')

from flask import Flask, request 
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))