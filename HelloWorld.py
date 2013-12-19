#Hello Application

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello there. I am here.'

if __name__ == '__main__':
    app.run()
