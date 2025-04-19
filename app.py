from flask import Flask, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify({
        "status": "✅ Jarvis 自動備份系統運行中",
        "time": datetime.utcnow().isoformat()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
