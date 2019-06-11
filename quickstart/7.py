from flask import Flask, session, redirect, url_for, escape, request

# session
app = Flask(__name__)

# set the secret key
app.secret_key = b'sdfasdfdsfsadfsdf'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in '

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form method='post'>
        <p><input type=text name=username>
        <p><input type=submit value=Login> 
    </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(
        debug= True,
        port = 5000,
        host = '0.0.0.0'
    )