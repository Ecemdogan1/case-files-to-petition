
import re
from datetime import datetime

date_pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"
money_pattern = r"\b\d+[\.,]?\d*\s?(TL|USD|EUR)\b"

def extract_entities(text):
    events = []
    dates = re.findall(date_pattern, text)
    monies = re.findall(money_pattern, text)

    for date in dates:
        try:
            parsed_date = datetime.strptime(date, "%d.%m.%Y").date()
        except:
            continue

        snippet = text[max(0, text.find(date)-60):text.find(date)+60]
        description = snippet.replace("\n", " ").strip()

        events.append({
            "date": str(parsed_date),
            "description": description,
            "money_mentions": monies
        })

    return events
