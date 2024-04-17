from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sensors")
def sensors():
    sensors = {
        "Umidade": 2, 
        "Temperatura": 23, 
        "Luminosidade": 1034
        }
    return render_template("sensors.html", devices=sensors, type="Sensores")

@app.route("/actuators")
def actuators():
    actuators = {
        "Servo": 122,
        "Lampada": 1
        }
    return render_template("actuators.html", devices=actuators, type="Atuadores")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)