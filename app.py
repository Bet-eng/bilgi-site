from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "SELAAMM KANKAAA LOVE YOUUU <3"

app.run(host="0.0.0.0", port=10000)