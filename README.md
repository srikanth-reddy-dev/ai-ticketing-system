# AI Ticketing System

## Overview

This project is a simple AI-powered ticketing system that automatically analyzes user issues and provides intelligent responses using rule-based logic.

---

## Features

* Create support tickets
* Automatic issue classification (Access, Billing, Other)
* Severity detection (High, Medium, Low)
* Auto-generated issue summary
* Sentiment detection (Frustrated, Neutral, Polite)
* Suggested resolution (Auto / Assign)
* Confidence score for prediction
* Automated response generation
* Feedback system (Yes / No)
* Real-time ticket display

---

## Tech Stack

* Frontend: HTML, JavaScript
* Backend: Python (Flask)
* Database: SQLite
* AI Logic: Rule-based system

---

## How It Works

1. User submits an issue through the UI
2. Backend analyzes keywords in the issue
3. System predicts:

   * Category
   * Severity
   * Summary
   * Sentiment
   * Resolution type
   * Confidence score
4. If issue is simple → auto response is generated
   If complex → assigned to support team
5. All tickets are stored and displayed dynamically

---

## Example Use Cases

* "login not working" → Access issue (High severity)
* "payment failed" → Billing issue (Medium severity)
* "general question" → Other (Low severity)

---

## Future Improvements

* Replace rule-based logic with real AI/ML models
* Add authentication and user roles
* Build analytics dashboard
* Add real-time notifications
* Deploy system to cloud

---

## Author

Srikanth Reddy
