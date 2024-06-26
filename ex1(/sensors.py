from flask import Flask, Blueprint, render_template, request, url_for

sensors = Blueprint("sensors", __name__, template_folder="templates_sensors")
devices = {
    "Umidade": 2,
    "Temperatura": 23,
    "Luminosidade": 1034
}


@sensors.route("/register_sensor")
def register_sensor():
    return render_template("register_sensor.html")


@sensors.route("/register_sensor_form", methods=["POST", "GET"])
def register_sensor_form():
    global devices
    if request.method == "POST":
        sensor = request.form["sensor"]
        reading = request.form["reading"]
    else:
        sensor = request.args.get("sensor", None)
        reading = request.args.get("reading", None)
    devices[sensor] = reading
    return render_template("list_sensors.html", dictionary=devices, dict_type="Sensores")


@sensors.route("/list_sensors")
def list_sensors():
    return render_template("list_sensors.html", dictionary=devices, dict_type="Sensores")


@sensors.route("/remove_sensor")
def remove_sensor():
    return render_template("remove_sensor.html", dictionary=devices)


@sensors.route("/del_sensor", methods=["GET", "POST"])
def del_sensor():
    global devices
    if request.method == "POST":
        sensor = request.form["sensor"]
    else:
        sensor = request.args.get("sensor", None)
    devices.pop(sensor)
    return render_template("list_sensors.html", dict_type="Sensores", dictionary=devices)
