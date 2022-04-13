#ECE 4564

from flask import Flask, render_template
import datetime
import time
import RPi.GPIO as GPIO

import sys

redPin = 21
greenPin = 20
bluePin = 16

def blink(pin, intensity):
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    pwm_led = GPIO.PWM(pin, 50)
    pwm_led.start(100)
    duty = int(intensity)
    pwm_led.ChangeDutyCycle(duty)
    time.sleep(0.5)
    #GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def redOn(intensity):
    blink(redPin, intensity)

def greenOn(intensity):
    blink(greenPin, intensity)

def blueOn(intensity):
    blink(bluePin, intensity)

def yellowOn(intensity):
    blink(redPin, intensity)
    blink(greenPin, intensity)

def cyanOn(intensity):
    blink(greenPin, intensity)
    blink(bluePin, intensity)

def magentaOn(intensity):
    blink(redPin, intensity)
    blink(bluePin, intensity)

def whiteOn(intensity):
    blink(redPin, intensity)
    blink(greenPin, intensity)
    blink(bluePin, intensity)

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

def turnOn(color, intensity):
    if color == "red":
        redOn(intensity)
    elif color == "green":
        greenOn(intensity)
    elif color == "blue":
        blueOn(intensity)
    elif color == "yellow":
        yellowOn(intensity)
    elif color == "cyan":
        cyanOn(intensity)
    elif color == "magenta":
        magentaOn(intensity)
    elif color == "white":
        whiteOn(intensity)

def main():
    while True:
        status = input("on or off?: ")
        if status == "on":
            color = input("color?: ")

            intensity = input("enter intensity value (0 to 100): ")
            whiteOff()
            turnOn(color, intensity)
        else:
            whiteOff()

    GPIO.cleanup()

main()





# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)