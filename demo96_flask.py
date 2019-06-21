from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello python using flask'


app.run(host='0.0.0.0', port=5001, debug=True)