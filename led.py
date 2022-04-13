#ECE 4564

from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO

redPin = 21
greenPin = 20
bluePin = 16

# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)