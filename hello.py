#!/usr/bin/env python

import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    s = 'This is an example:' + socket.gethostname() 
    return s

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
