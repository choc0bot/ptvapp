from flask import Flask

application = flask.Flask(__name__)
from app import views
