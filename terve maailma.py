from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return input("Write something: ")

app.run(port="8000")
