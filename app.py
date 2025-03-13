from flask import Flask
from flask.ctx import F

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

print(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)