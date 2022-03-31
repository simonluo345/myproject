from app import myobj
from flask import render_template, flash, request

city_names = ["Paris", "London", "Rome", "Tahiti"]


@myobj.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        flash(request.form["nm"])
    return render_template("home.html", title="The Blog", city=city_names)
