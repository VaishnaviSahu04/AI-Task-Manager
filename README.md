# 🚀 AI Task Manager

An AI-powered workflow system that converts unstructured meeting text into structured, actionable tasks using FastAPI.

---

## 📌 Problem Statement

In meetings, important tasks are often buried in long conversations. Manually extracting tasks, assigning owners, and tracking deadlines is time-consuming and error-prone.

---

## 💡 Solution

This system automatically:
- Extracts tasks from natural language input
- Identifies task owners
- Detects deadlines (today, tomorrow, next week)
- Assigns priority (High, Medium, Low)
- Tracks status (Pending, Completed, Overdue)

---

## ⚙️ Features

- 🧠 AI-based task extraction
- 📅 Deadline detection
- 🔥 Priority classification
- 📊 Real-time dashboard
- ✅ Task status update
- ❌ Task deletion
- 🔍 Search functionality
- 📈 Task statistics (Total, Pending, Completed, Overdue)

---

## 🏗️ Architecture
User Input → Extraction → Priority Assignment → Storage → Monitoring → UI

### Agents:
- Input Agent
- Extraction Agent
- Priority Agent
- Execution Agent
- Monitoring Agent

---

## 🔗 Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **API Testing:** Swagger UI

---

## 🔄 API Endpoints

| Method | Endpoint | Description |
|-------|--------|-------------|
| GET | `/` | Check server |
| POST | `/add_meeting` | Extract tasks |
| GET | `/get_tasks` | Fetch tasks |
| PUT | `/update_status/{id}` | Update status |
| DELETE | `/delete_task/{id}` | Delete task |

---

## ▶️ How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```
Open:

http://127.0.0.1:8000

Swagger API:

http://127.0.0.1:8000/docs (paste on browser)

Example Input

Rahul must finish backend today urgently, Priya should complete UI tomorrow, testing can be done next week

Output:

Task 1: Rahul → High Priority → Today
Task 2: Priya → Medium → Tomorrow
Task 3: Testing → Low → Next Week
📊 Impact
⏱ Manual effort: ~2 min/task
⚡ AI effort: ~10 sec/task
🔥 ~90% time reduction

Monthly (20 meetings):

⏳ ~3+ hours saved
🛡️ Error Handling
Missing owner → Assigned "Unknown"
Missing deadline → Default handled
Invalid input → Safely ignored
API failure → Response validation
Format issues → No system crash

📸 Demo Screenshots

<img width="379" height="412" alt="{1E69A45F-7169-4F92-95F0-966FACADD3A5}" src="https://github.com/user-attachments/assets/33bbe61e-6557-4d0e-b2a6-e8944a61d691" />

<img width="863" height="411" alt="{104CC65A-D8B7-4DD4-870B-7688D37EA59D}" src="https://github.com/user-attachments/assets/78048afd-4ec9-4657-b5d6-5222d44cf6b5" />


🚀 Future Enhancements
NLP model integration (BERT / GPT)
Email & Slack integration
Notifications & reminders
Multi-user system
Cloud deployment

👩‍💻 Author

Vaishnavi Sahu

⭐ Note

Python 3.10+ supports namespace packages, so __init__.py is optional in the utils folder.


---
