from flask import Flask
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Home page accessed successfully")
    return """
    <h1>AKS Observability Capstone</h1>
    <p>Application is running on AKS and monitored using Azure Monitor + Container Insights.</p>
    <ul>
      <li>/health - Health check</li>
      <li>/cpu - Generate CPU load</li>
      <li>/error - Generate error log</li>
      <li>/crash - Simulate pod crash</li>
    </ul>
    """

@app.route("/health")
def health():
    app.logger.info("Health endpoint checked")
    return {"status": "healthy", "service": "aks-observability-app"}

@app.route("/cpu")
def cpu_load():
    app.logger.warning("CPU load endpoint triggered")
    end_time = time.time() + 10
    while time.time() < end_time:
        _ = sum(i * i for i in range(10000))
    return "CPU load generated for monitoring test"

@app.route("/error")
def error_log():
    app.logger.error("Sample ERROR log generated for Azure Monitor KQL testing")
    return "Error log generated. Check Container Logs in Log Analytics."

@app.route("/crash")
def crash():
    app.logger.critical("Crash endpoint triggered. Pod will exit intentionally.")
    os._exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
