from flask import Flask, jsonify, render_template
from prometheus_flask_exporter import PrometheusMetrics
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/", methods=['GET'])
def home():
    logger.info("Home endpoint hit")
    return render_template('index.html')

@app.route("/health", methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route("/simulate-error", methods=['GET'])
def simulate_error():
    if random.random() < 0.5:
        logger.error("Simulated 500 error!")
        return jsonify({"error": "Something went wrong"}), 500
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)