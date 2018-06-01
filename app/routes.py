from app import app
from .door import Door

@app.route('/')
@app.route('/index')
def index():
    return ""

@app.route('/login', methods=['POST'])
def login():
    return 'done'

@app.route('/door/open', methods=['POST'])
def open_door():
    door = Door()
    return door.open()
