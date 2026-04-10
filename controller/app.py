from flask import Flask, request, jsonify

app = Flask(__name__)
metrics_store = []

@app.route("/metrics", methods=["POST"])
def receive_metrics():
    data = request.json
    metrics_store.append(data)
    return jsonify({"status": "received"})

@app.route("/metrics", methods=["GET"])
def get_metrics():
    return jsonify(metrics_store)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
