from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bedroom")
def bedroom():
    return render_template("bedroom.html")

@app.route("/bedroom/sensors")
def bedroom_sensors():
    sensors = ["Temperatura","Luminosidade"]
    return render_template("bedroom_sensor.html", sensors=sensors)

@app.route("/bedroom/actuators")
def bedroom_actuators():
    actuators = ["Interruptor", "Ar-condicionado"]
    return render_template("bedroom_actuators.html", actuators=actuators)

@app.route("/bathroom")
def bathroom():
    return render_template("bathroom.html")
@app.route("/bathroom/sensors")
def bathroom_sensors():
    sensors = ["Umidade"]
    return render_template("bathroom_sensors.html", sensors=sensors)

@app.route("/bathroom/actuators")
def bathroom_actuators():
    actuators = ["Lampada","Ventoinha"]
    return render_template("bathroom_actuators.html", actuators=actuators)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)