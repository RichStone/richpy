from flask import Flask
app = Flask(__name__)
print(app)

@app.route('/')
def index():
    return '<h1>RichPy!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hey, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)