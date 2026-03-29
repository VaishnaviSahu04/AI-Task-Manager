import sqlite3

def create_connection():
    return sqlite3.connect("tasks.db")


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        owner TEXT,
        deadline TEXT,
        priority TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_task(task, owner, deadline, priority="Medium", status="Pending"):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks (task, owner, deadline, priority, status)
    VALUES (?, ?, ?, ?, ?)
    """, (task, owner, deadline, priority, status))

    conn.commit()
    conn.close()


def get_all_tasks():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.close()
    return rows


def update_task_status(task_id, status):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET status=?
    WHERE id=?
    """, (status, task_id))

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()


# 🔥 NEW: Clear all tasks (prevents duplicates)
def clear_tasks():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks")

    conn.commit()
    conn.close()