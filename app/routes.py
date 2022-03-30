from app import myobj
from flask import render_template, flash, request


@myobj.route("/", methods=["POST", "GET"])
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    if request.method == "POST":
        flash(request.form["nm"])
    return render_template("home.html", title="The Blog", name=name, city=city_names)


@myobj.route("/<name>")
def user(name):
    return f"hello {name}"
