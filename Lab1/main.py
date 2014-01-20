from flask import Flask, render_template, abort
from jinja2 import Template


app = Flask(__name__)
app.debug = True
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = "##"
files = ["favicon.ico", "style.css"]
@app.route('/')
def landing():
    return render_template("landing.html", pythoncode=open("main.py").read())

@app.route('/about')
def about():
    return render_template("about.html", gustavs_code=open("gustavskod.rb").read())

@app.route('/<what>')
def default(what=None):
    if what in files:
        return open(what).read()
    else:
        return abort(404)

if __name__ == '__main__':
    app.run()
