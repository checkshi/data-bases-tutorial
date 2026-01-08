from flask import Flask, g, redirect, render_template, request, url_for
import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "data.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()

app = Flask(__name__)

@app.before_request
def ensure_database():
    if not DATABASE_PATH.exists():
        init_db()

def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

app.teardown_appcontext(close_db)

@app.route("/", methods=["GET"])
def index():
    db = get_db()
    guests = db.execute(
        "SELECT id, name, email, message, created_at FROM guests ORDER BY created_at DESC"
    ).fetchall()
    return render_template("index.html", guests=guests)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if name and email and message:
        db = get_db()
        db.execute(
            "INSERT INTO guests (name, email, message) VALUES (?, ?, ?)",
            (name, email, message),
        )
        db.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
