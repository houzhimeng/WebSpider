# coding=utf-8
from flask import Flask

app = Flask(__name__)
@app.route("/<user>")
def hello(user):
    if user == 'admin':
        return "<h1>管理员，您好！<h1>"
    else:
        return "<h1>%s, 您好！</h1>" % user
if __name__ == "__main__":
    app.run()


