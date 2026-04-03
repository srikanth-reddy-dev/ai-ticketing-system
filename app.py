from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            issue TEXT,
            category TEXT,
            priority TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def classify_ticket(issue):
    issue = issue.lower()
    if "salary" in issue:
        return "HR", "Medium"
    elif "login" in issue or "system" in issue:
        return "IT", "High"
    elif "payment" in issue:
        return "Finance", "High"
    else:
        return "General", "Low"

@app.route('/create', methods=['POST'])
def create_ticket():
    data = request.json
    name = data['name']
    issue = data['issue']

    category, priority = classify_ticket(issue)

    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("INSERT INTO tickets (name, issue, category, priority, status) VALUES (?, ?, ?, ?, ?)",
              (name, issue, category, priority, "Open"))
    conn.commit()
    conn.close()

    return jsonify({"message": "Ticket created", "category": category, "priority": priority})

@app.route('/tickets', methods=['GET'])
def get_tickets():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tickets")
    rows = c.fetchall()
    conn.close()

    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)