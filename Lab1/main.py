from flask import Flask, render_template
from jinja2 import Template


app = Flask(__name__)
app.debug = True
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = "##"

@app.route('/')
def landing():
    return render_template("landing.html", names=["Gustav", "Filip"])

@app.route('/about')
def about():
    return render_template("about.html", names=["Gustav", "Filip"])

@app.route('/<what>')
def noname(what=None):
    return open(what).read()


if __name__ == '__main__':
    app.run()
