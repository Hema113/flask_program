from flask import Flask,request,url_for,session,escape,redirect

app = Flask(__name__)

app.secret_key = 'FG_20#123FGCBD'

@app.route('/')
def index():
    if 'username' in session:
        user = session['username']
        return 'log in as {}'.format(user)
    return 'you are not loged in'

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method='post'>
        Username:<input type=text name=username></br>
        <input type =submit value=login>
        </form>
        '''
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
