from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("welcome.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
