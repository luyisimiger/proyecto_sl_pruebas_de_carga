from flask import current_app, Blueprint, render_template, redirect, url_for, request
from flaskapp.logic.ab import runab

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html")


@views.route('/ab', methods=["GET", "POST"])
def ab_get():

    url = "http://www.github.com/"
    n = "20"
    c = "5"

    if request.json:
        print(request.json)
        c = str(request.json['c'])
        n = str(request.json['n'])
        url = str(request.json['url'])

    
    args = ["ab", "-c", c, "-n", n, url]
    print(args)
    result = runab(args)
    # return render_template("ab.html")
    return result
