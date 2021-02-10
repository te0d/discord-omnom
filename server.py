from flask import Flask, render_template
from message_db import MessageDatabase

app = Flask(__name__)
db = MessageDatabase()

@app.route('/')
def index():
    messages = db.get_messages()
    return render_template('messages.html', messages=messages)
