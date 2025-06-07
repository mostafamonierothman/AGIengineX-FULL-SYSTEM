# debug/debug_logger.py

import datetime

def log_info(message):
    timestamp = datetime.datetime.utcnow().isoformat()
    print(f"[{timestamp}] {message}")
