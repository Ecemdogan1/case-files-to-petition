
def build_timeline(events):
    sorted_events = sorted(events, key=lambda x: x["date"])
    return sorted_events
