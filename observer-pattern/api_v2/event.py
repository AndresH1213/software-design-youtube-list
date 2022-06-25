"""simple event implementation"""
subscribers = dict()


def subscribe(event_type: str, fn):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, data):
    # map of events an call the function in it
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)
