#ECE 4564

from flask import Flask, render_template
import datetime
import time
import RPi.GPIO as GPIO

import sys

redPin = 21
greenPin = 20
bluePin = 16

def blink(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setmode(GPIO.BCM)
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

def turnOn(color, intensity):
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
#
#


def main():
    # while True:
    #     status = input("on or off?: ")
    #     if status == "on":
    #         color = input("color?: ")
    #         intensity = input("enter intensity value (0 to 100): ")
    #         duty = int(intensity)
    #         pwm_led = GPIO.PWN()
    #         whiteOff()
    #         turnOn(color, intensity)
    #     else:
    #         whiteOff()
    led = redPin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    # 50Hz PWM Frequency
    pwm_led = GPIO.PWM(led, 50)
    # Full Brightness, 100% Duty Cycle
    pwm_led.start(100)
    try:
        while True:
            duty_s = input("Enter Brightness Value (0 to 100):")
            # Convert into Integer Value  
            duty = int(duty_s)
            pwm_led.ChangeDutyCycle(duty)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print
        "Exiting Program"
    except:
        print
        "Error Occurs, Exiting Program"
    finally:
        GPIO.cleanup()
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