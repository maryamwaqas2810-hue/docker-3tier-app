from flask import Flask, jsonify

app = Flask(__name__)

items = ["Docker seekhna", "Compose banana", "AWS pe deploy karna"]

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/items")
def get_items():
    return jsonify(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)