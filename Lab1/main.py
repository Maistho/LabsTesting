from flask import Flask, render_template
from jinja2 import Template


app = Flask(__name__)
app.debug = True
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = "##"

@app.route('/')
def hello_world():
    return render_template("template1.html", names=["Gustav", "Filip"])


if __name__ == '__main__':
    app.run()
