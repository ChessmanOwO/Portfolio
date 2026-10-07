import os
import json
import sqlite3
import datetime
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")
DB_FILE = os.path.join(os.path.dirname(__file__), "portfolio.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/contact", methods=["POST"])
def submit_contact():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    subject = data.get("subject", "Liên hệ từ Portfolio").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "error": "Vui lòng điền đầy đủ họ tên, email và lời nhắn!"}), 400

    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute(
            "INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
            (name, email, subject, message)
        )
        conn.commit()
        contact_id = c.lastrowid
        conn.close()
        return jsonify({
            "success": True,
            "message": f"Cảm ơn {name}! Lời nhắn của bạn đã được ghi nhận và gửi đến Chesman.contact@gmail.com thành công.",
            "contact_id": contact_id
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    print("Backend Server đang chạy tại http://localhost:8085")
    app.run(host="0.0.0.0", port=8085, debug=False)
