import flask
from pixellib import pixel
from snake import setdirection
app = flask.Flask (__name__)
app.config["DEBUG"] = False


@app.route('/an', methods = ['GET'])
def white ():
    pixel(6,6,"white")
    setdirection("up")
    return "<h1>is an jetzt</h1>"

@app.route('/aus', methods = ['GET'])
def off ():
    pixel(6,6,"off")
    setdirection("down")
    return "<h1>is aus jetzt</h1>"

app.run(host='0.0.0.0')