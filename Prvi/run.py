from flask import Flask
app=flask(__name__)

APP_ADRESS="0.0.0.0"
APP_PORT=5000

app.config["DEBUG"]=True
app.run(host=APP_ADRESS, port=APP_PORT)

@app.route("/")
def hello_world():
    return "Hello World"
