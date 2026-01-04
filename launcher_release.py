# launcher_release.py
from launcher_core import run_stages

STAGES = [
    {"id": 0, "script": "1_health_check.py"},
    {"id": 1, "script": "2_relay_check.py"},
    {"id": 2, "script": "2_1_extra_checks.py"},
    {"id": 3, "script": "motor_release.py"},
    {"id": 4, "script": "weed_autonomous.py"}
]

run_stages(STAGES)
