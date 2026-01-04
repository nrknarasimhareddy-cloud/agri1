# safety.py
import os
from config import DEBUG, PRETEST_FLAG

def pretests_passed():
    if DEBUG:
        return True
    return os.path.exists(PRETEST_FLAG)
