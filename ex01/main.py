from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Minha casa</title>
        </head>
        <body>
            <h2>Minha casa</h2>
            <h3>Acesse o menu:</h3>
            <ul>
                <li><a href="/sensors">Listar Sensores</a></li>
                <li><a href="/actuators">Listar Atuadores</a></li>
            </ul>
        </body>
    </html>
    """

@app.route("/sensors")
def sensors():
    return """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Sensores</h1>
            <ul>
                <li>Sensor de umidade</li>
                <li>Sensor de Temperatura</li>
                <li>Sensor de Luminosidade</li>
            </ul>
            <a href="/">
                <p>Voltar para pagina inicial</p>
            </a>
        </body>
    </html>
"""

@app.route("/actuators")
def actuators():
    return """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Atuadores</h1>
            <ul>
                <li>Servo motor</li>
                <li>Sensor de Temperatura</li>
            </ul>
            <a href="/">
                <p>Voltar para pagina inicial</p>
            </a>
        </body>
    </html>
    """ 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    app.run(debug=True)