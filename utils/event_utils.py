def get_event_date(event):
    return str(event).split("T")[0]

def get_event_start_time(event):
    return str(str(event).split("T")[1])[0:6]

def get_event_end_time(event):
    yield

def get_events_by_date(events):
    yield