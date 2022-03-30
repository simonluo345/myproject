from flask import Flask

myapp = Flask(__name__)
myapp.config.from_mapping(SECRET_KEY="you-will-never-guess")

from app import routes