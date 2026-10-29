import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT NOT NULL)")
    cur.execute("SELECT COUNT(*) FROM items")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO items (name) VALUES (%s)",
            [("Docker seekhna",), ("Compose banana",), ("AWS pe deploy karna",)],
        )
    conn.commit()
    cur.close()
    conn.close()


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/items")
def get_items():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name FROM items ORDER BY id")
    rows = [r[0] for r in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(rows)


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)