from flask import Flask, redirect, render_template
from flask import request


app = Flask(__name__)
print(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/redir')
def redir():
    return redirect('https://www.amazon.com')

if __name__ == '__main__':
    app.run(debug=True)