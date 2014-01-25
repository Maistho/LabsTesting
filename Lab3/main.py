from flask import Flask, render_template, abort, request, redirect
from flask_wtf import Form
from wtforms import TextField
from database import Database
from my_forms import RegistrationForm


app = Flask(__name__)
app.debug = True
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = "##"
files = ["favicon.ico", "style.css"]
db = Database()
@app.route('/')
def landing():
    return render_template("landing.html", pythoncode=open("main.py").read())

@app.route('/about')
def about():
    return render_template("about.html", gustavs_code=open("gustavskod.rb").read())

@app.route('/register', methods=["GET", "POST"])
def register():
    my_form = RegistrationForm(request.form)
    if request.method == 'POST' and my_form.validate():
        db.create_user(my_form.data)
        return redirect('/')
    people = db.users()
    people_str = str(people) + " person" + ("s have" if (people > 1) else " has")
    return render_template("register.html", form=my_form, people=people_str)

@app.route('/<what>')
def default(what=None):
    if what in files:
        return open(what).read()
    else:
        return abort(404)

@app.route('/drop')
def drop_table():
    db.reset()
    return "users dropped"

if __name__ == '__main__':
    app.run()
