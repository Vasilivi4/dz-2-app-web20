from flask import Flask

app = Flask(__name__)


@app.route("/")
def test_docker_box():
    return "<h1>☻{<(Tuk-Tuk)>}☻</h1>" "<h1>♥☺___$;-)|=___☺♥</h1>"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
