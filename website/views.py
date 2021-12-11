from flask import Blueprint, render_template
from website import templates


views = Blueprint('views', __name__)


@views.route('/')


def home():
    return render_template("base.html")


@views.route('/templates/support.html')


def support():
    return render_template("support.html")

@views.route('/templates/base.html')
def home2():
    return render_template("base.html")
@views.route('templates/about.html')
def about():
    return render_template("about.html")
