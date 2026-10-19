# SYSTEM LIBRARIES
from flask import Flask
from flask import render_template
from flask import request

# MY LIBRARIES
from module import dbConfig
from module import dbLogic

app = Flask(__name__)

APP_ADDRESS = "0.0.0.0"
APP_PORT = 5000

@app.route("/", methods = ["GET","POST"])
def index():
    data = {
        "uspeh" : False,
        "itm" : None,
        "teza": "",
        "visina": ""
    }
    data["uspeh"] = dbLogic.getAll()
    if request.method == "POST":
        data["teza"] = request.form.get("teza")
        data["visina"] = request.form.get("visina")
        if data["teza"] and data["visina"]:
            data["itm"] = izracunaj_itm(float(data["visina"]), float(data["teza"]))
            dbLogic.insertData(float(data["visina"]), float(data["teza"]), float(data["itm"]))
        print(data)
    return render_template("index.html", podatki = data)


def izracunaj_itm(visinaCm, teza):
    itm = teza / (visinaCm/100) ** 2
    return itm

@app.route("/dnevnik", methods = ["GET", "POST"])
def dnevnik():
    data = {}

    data["seznam"] = dbLogic.getAll()

    return render_template("dnevnik.html", podatki = data)

app.config["DEBUG"] = True
app.run(host = APP_ADDRESS, port = APP_PORT)