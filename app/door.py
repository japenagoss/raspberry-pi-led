import RPi.GPIO as GPIO
import time
from flask import jsonify

class Door():
    def open(self):
        channel  = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, True)
        time.sleep(2);
        GPIO.output(channel, False)
        GPIO.cleanup(channel)
        reply = {'success':True}
        return jsonify(reply)
