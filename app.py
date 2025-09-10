from flask import Flask

app = Flask(__name__)

from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "🚀 Hello from Cloud Counselage Internship Project!!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#test
