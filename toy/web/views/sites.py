from flask import Blueprint, render_template

module = Blueprint("site", __name__)


@module.route("/")
def index():
    return render_template(
        'index.html',
        header='asdfghjk'
    )

@module.route("/hello")
def hello():
    return render_template(
        'hello.html',
    )

@module.route("/info")
def info():
    return render_template(
        'info.html',
    )

@module.route("/my")
def my():
    return render_template(
        'my.html',
    )

@module.route("/js")
def js():
    return render_template(
        'js.html',
    )

@module.route("/new")
def new():
    return render_template(
        'new.html',
    )

@module.route("/hi")
def hi():
    return render_template(
        'hi.html',
    )

@module.route("/firebase")
def firebase():
    return render_template(
        'firebase.html',
    )
