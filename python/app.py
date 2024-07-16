# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<b>Hello,</b><br><b>Python Application from Docker & Docker-compose!!!</b>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
