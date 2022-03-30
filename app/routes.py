from app import myapp
from flask import render_template, flash, request

@myapp.route("/", methods=["POST", "GET"])
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    if request.method == "POST":
        flash(request.form["nm"])
    return render_template("home.html", title="The Blog", name=name, city=city_names)


@myapp.route("/<name>")
def user(name):
    return f"hello {name}"

