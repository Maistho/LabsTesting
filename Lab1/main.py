from flask import Flask
from jinja2 import Template
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    template = Template(open("Templates/template1.html").read())
    return template.render(name="Gustav")


if __name__ == '__main__':
    app.run()
