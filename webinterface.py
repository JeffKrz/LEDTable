#!/usr/bin/env python3
import flask
from pixellib import pixel
app = flask.Flask (__name__)
app.config["DEBUG"] = False


@app.route('/up', methods = ['GET'])
def up ():
    f = open("direction.txt", "w")
    f.write("up")
    f.close()
    return "nix"

@app.route('/down', methods = ['GET'])
def down ():
    f = open("direction.txt", "w")
    f.write("down")
    f.close()
    return "nix"

@app.route('/left', methods = ['GET'])
def left ():
    f = open("direction.txt", "w")
    f.write("left")
    f.close()
    return "nix"

@app.route('/right', methods = ['GET'])
def right ():
    f = open("direction.txt", "w")
    f.write("right")
    f.close()
    return "nix"

app.run(host='0.0.0.0')