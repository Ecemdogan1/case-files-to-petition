
from extractor import extract_entities
from timeline import build_timeline
from legal_classifier import classify_dispute
from petition_builder import build_petition
import os
import json

CASE_DIR = "case_files"

def read_case_files():
    texts = []
    for file in os.listdir(CASE_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(CASE_DIR, file), "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts

def main():
    print("Reading case files...")
    texts = read_case_files()

    print("Extracting entities and events...")
    events = []
    for text in texts:
        events.extend(extract_entities(text))

    print("Building timeline...")
    timeline = build_timeline(events)

    print("Classifying dispute type...")
    dispute_type = classify_dispute(texts)

    print("Building petition draft...")
    petition = build_petition(timeline, dispute_type)

    with open("timeline.json", "w", encoding="utf-8") as f:
        json.dump(timeline, f, indent=4, ensure_ascii=False)

    with open("case_summary.txt", "w", encoding="utf-8") as f:
        for event in timeline:
            f.write(f"{event['date']} - {event['description']}\n")

    with open("petition_draft.txt", "w", encoding="utf-8") as f:
        f.write(petition)

    print("Outputs generated: timeline.json, case_summary.txt, petition_draft.txt")

if __name__ == "__main__":
    main()
