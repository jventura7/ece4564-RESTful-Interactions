#ECE 4564

from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
import sys

redPin = 21
greenPin = 20
bluePin = 16

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def redOn():
    blink(redPin)

def greenOn():
    blink(greenPin)

def blueOn():
    blink(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def redOff():
    turnOff(redPin)

def greenOff():
    turnOff(greenPin)

def blueOff():
    turnOff(bluePin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)

def turnOn(status, color, intensity):
    if status == "off":
        whiteOff()
    if color == "red":
        redOn()
    elif color == "green":
        greenOn()
    elif color == "blue":
        blueOn()
    elif color == "yellow":
        yellowOn()
    elif color == "cyan":
        cyanOn()
    elif color == "magenta":
        magentaOn()
    elif color == "white":
        whiteOn()


def main():
    while True:
        status = input("on or off?: ")
        color = input("color?: ")
        intensity = input("intensity?: ")
        turnOn(status, color, intensity)

# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)