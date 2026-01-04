# robot_core/
#│
#├── config.py
#├── gpio_map.py
#├── logger.py
#├── safety.py
#│
#├── motor_core.py
#├── launcher_core.py
#│
#├── motor_debug.py
#├── motor_release.py
#│
#├── launcher_debug.py
#├── launcher_release.py

# config.py

MODE = "RELEASE"        # 🔁 change ONCE: DEBUG / RELEASE

DEBUG = MODE == "DEBUG"

LOG_DIR = "/home/pi/logs"

PRETEST_FLAG = "/home/pi/pretests_passed.flag"

STAGE_TIMEOUT = 9999 if DEBUG else 120
