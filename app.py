from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/cpu")
def cpu():
    return jsonify(cpu_percent=psutil.cpu_percent(interval=1))

@app.route("/memory")
def memory():
    mem = psutil.virtual_memory()
    return jsonify(used=mem.used, total=mem.total, percent=mem.percent)

@app.route("/disk")
def disk():
    disk = psutil.disk_usage("/")
    return jsonify(used=disk.used, total=disk.total, percent=disk.percent)

@app.route("/uptime")
def uptime():
    return jsonify(uptime_seconds=int(time.time() - START_TIME))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
