import re
from datetime import datetime, timedelta

def parse_deadline(text):
    text = text.lower()

    today = datetime.today()

    if "today" in text:
        return today.strftime("%Y-%m-%d")
    elif "tomorrow" in text:
        return (today + timedelta(days=1)).strftime("%Y-%m-%d")
    elif "next week" in text:
        return (today + timedelta(days=7)).strftime("%Y-%m-%d")
    elif "friday" in text:
        # next Friday logic
        days_ahead = (4 - today.weekday()) % 7
        days_ahead = 7 if days_ahead == 0 else days_ahead
        return (today + timedelta(days=days_ahead)).strftime("%Y-%m-%d")

    return today.strftime("%Y-%m-%d")


def detect_priority(text):
    text = text.lower()

    if "urgent" in text or "asap" in text or "today" in text:
        return "High"
    elif "tomorrow" in text or "soon" in text:
        return "Medium"
    elif "next week" in text or "later" in text:
        return "Low"
    else:
        return "Medium"


def extract_tasks(text):
    tasks = []

    sentences = re.split(r'and|,|\.', text)

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        words = sentence.split()
        owner = "Unknown"

        if words and words[0][0].isupper():
            owner = words[0]

        deadline = parse_deadline(sentence)
        priority = detect_priority(sentence)

        tasks.append({
            "task": sentence,
            "owner": owner,
            "deadline": deadline,
            "priority": priority
        })

    return tasks