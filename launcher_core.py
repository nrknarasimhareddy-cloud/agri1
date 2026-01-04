# launcher_core.py
import subprocess
from datetime import datetime
from config import STAGE_TIMEOUT
from logger import log

LOG_FILE = "launcher.log"

def run_stages(stages):
    for stage in stages:
        sid = stage["id"]
        cmd = ["python3", stage["script"]] + stage.get("args", [])

        log(f"STAGE {sid} START: {' '.join(cmd)}", LOG_FILE)

        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=STAGE_TIMEOUT
            )
            log(result.stdout, LOG_FILE)

            if result.returncode != 0:
                log(f"STAGE {sid} FAILED", LOG_FILE)
                return False

        except Exception as e:
            log(f"STAGE {sid} CRASH: {e}", LOG_FILE)
            return False

        log(f"STAGE {sid} PASSED", LOG_FILE)

    return True
