from flask import Flask, render_template
from jinja2 import Template


app = Flask(__name__)
app.debug = True
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = "##"

@app.route('/')
def hello_world():
    return render_template("start.html", title="Start page", names=["Gustav", "Filip"])

@app.route('/<what>')
def noname(what=None):
    return open(what).read()


if __name__ == '__main__':
    app.run()
