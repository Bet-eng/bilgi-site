from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "SELAAMM KANKAAA LOVE YOUUU <3"

app.run(host="0.0.0.0", port=10000)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hakkimda")
def hakkimda():
    return render_template("hakkimda.html")

@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)