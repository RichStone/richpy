from flask import Flask
app = Flask(__name__)
print(app)

@app.route('/')
def index():
    return '<h1>RichPy!</h1>'

if __name__ == '__main__':
    app.run(debug=True)