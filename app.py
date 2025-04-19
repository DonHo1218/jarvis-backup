from flask import Flask, jsonify, render_template
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify({"status": "✅ Jarvis 自動備份系統運行中", "time": datetime.utcnow().isoformat()})

if __name__ == "__main__":
    app.run(debug=True)
