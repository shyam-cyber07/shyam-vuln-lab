from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Shyam Vulnerable Lab (Public)</h1>"

@app.route("/login")
def login():
    user = request.args.get("user")
    return f"Welcome {user}"

@app.route("/search")
def search():
    q = request.args.get("q")
    return q

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
