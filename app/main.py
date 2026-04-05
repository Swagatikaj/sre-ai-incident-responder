from flask import Flask, jsonify
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    logger.info("Home endpoint hit")
    return jsonify({"status": "ok", "message": "SRE AI App running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/simulate-error")
def simulate_error():
    # Simulates a random failure — useful for testing alerts later
    if random.random() < 0.5:
        logger.error("Simulated 500 error!")
        return jsonify({"error": "Something went wrong"}), 500
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
