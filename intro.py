from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def f_page(name):
    return 'Hello %s!'%name

if __name__ == '__main__':
    app.run()
