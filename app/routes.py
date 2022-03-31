from app import myobj
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    cityname = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@myobj.route("/", methods=["POST", "GET"])
def home():
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    name = "Lisa"
    form = LoginForm()
    if form.validate_on_submit():
        flash("{}".format(form.cityname.data))
    return render_template("home.html", title="The Blog", city=city_names, name=name, form=form)
