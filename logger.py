# logger.py
from datetime import datetime
from config import DEBUG, LOG_DIR

def log(msg, file):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"

    if DEBUG:
        print(line)

    with open(f"{LOG_DIR}/{file}", "a") as f:
        f.write(line + "\n")
