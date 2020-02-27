from datetime import datetime
import time

def get_timestamp():
    return datetime.now().timestamp()

def generate_ticket(email):
    ts = time.time()
    dt = datetime.fromtimestamp(ts)
    ticket = dt.strftime('%Y%m%d%H%M%S-') + email
    return ticket