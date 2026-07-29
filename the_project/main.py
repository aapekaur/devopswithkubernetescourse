import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return {"message": "Hello from Flask running in Docker!"}


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port_number = os.environ["PORT"]
    print(f"Server started in port {port_number}")
    app.run(host="0.0.0.0", port=port_number)
