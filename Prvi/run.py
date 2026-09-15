from flask import Flask
from flask import render_template

app=Flask(__name__)

APP_ADRESS="0.0.0.0"
APP_PORT=5000

app.config["DEBUG"]=True
app.run(host=APP_ADRESS, port=APP_PORT)

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return render_template("index.html")

app.config["DEBUG"] = True
app.run(host = APP_ADRESS, port = APP_PORT)