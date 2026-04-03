from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# -------------------------
# DB INIT
# -------------------------
def init_db():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            issue TEXT,
            category TEXT,
            severity TEXT,
            summary TEXT,
            sentiment TEXT,
            resolution TEXT,
            confidence TEXT,
            status TEXT,
            auto_reply TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# -------------------------
# AI LOGIC (RULE BASED)
# -------------------------
def classify_ticket(issue):
    issue = issue.lower()

    if any(word in issue for word in ["login", "password", "signin"]):
        return {
            "category": "Access",
            "severity": "High",
            "summary": "User facing login issue",
            "sentiment": "Frustrated",
            "resolution": "Auto",
            "confidence": "90%"
        }

    elif any(word in issue for word in ["payment", "refund", "billing"]):
        return {
            "category": "Billing",
            "severity": "Medium",
            "summary": "Payment related issue",
            "sentiment": "Neutral",
            "resolution": "Assign",
            "confidence": "85%"
        }

    else:
        return {
            "category": "Other",
            "severity": "Low",
            "summary": "General query",
            "sentiment": "Polite",
            "resolution": "Assign",
            "confidence": "70%"
        }

# -------------------------
# CREATE TICKET
# -------------------------
@app.route('/create', methods=['POST'])
def create_ticket():
    data = request.json
    name = data['name']
    issue = data['issue']

    result = classify_ticket(issue)

    # Auto response
    if result["resolution"] == "Auto":
        auto_reply = "Please reset your password using the reset option. If issue persists, contact IT support."
    else:
        auto_reply = "Your issue has been assigned to support team."

    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO tickets 
        (name, issue, category, severity, summary, sentiment, resolution, confidence, status, auto_reply)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        name,
        issue,
        result["category"],
        result["severity"],
        result["summary"],
        result["sentiment"],
        result["resolution"],
        result["confidence"],
        "New",
        auto_reply
    ))

    conn.commit()
    conn.close()

    return jsonify({"message": "Ticket created"})

# -------------------------
# GET TICKETS
# -------------------------
@app.route('/tickets', methods=['GET'])
def get_tickets():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()

    c.execute("SELECT * FROM tickets")
    rows = c.fetchall()

    conn.close()
    return jsonify(rows)

# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)