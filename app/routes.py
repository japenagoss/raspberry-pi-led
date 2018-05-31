import RPi.GPIO as GPIO
import time
from app import app

@app.route('/')
@app.route('/index')
def index():
    return ""

@app.route('/login', methods=['POST'])
def login():
    return 'done'

@app.route('/door/open', methods=['POST'])
def open():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, True)
    time.sleep(2);
    GPIO.output(17, False)
    GPIO.cleanup()
    return True;
