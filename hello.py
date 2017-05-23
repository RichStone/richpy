from flask import Flask, redirect
from flask import request

app = Flask(__name__)
print(app)

@app.route('/')
def index():
    return '<h1>RichPy!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hey, %s!</h1>' % name

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/redir')
def redir():
    return redirect('https://www.amazon.com')

if __name__ == '__main__':
    app.run(debug=True)