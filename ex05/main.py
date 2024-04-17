from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sensors")
def sensors():
    sensors = ["Umidade", "Temperatura", "Luminosidade"]
    return render_template("sensors.html", sensors=sensors)

@app.route("/actuators")
def actuators():
    actuators = ["Lampada","Ventoinha"]
    return render_template("actuators.html", actuators=actuators)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)