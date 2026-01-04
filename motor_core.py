# motor_core.py
import RPi.GPIO as GPIO
import time
import signal
import sys

from gpio_map import *
from safety import pretests_passed
from logger import log

LOG_FILE = "motor.log"

speed_map = {
    1: 20,
    2: 40,
    3: 60,
    4: 80
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(FAULT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(PWM_PIN, 1000)
pwm.start(0)

def motor_off():
    pwm.ChangeDutyCycle(0)
    GPIO.output(RELAY_PIN, GPIO.LOW)
    log("Motor OFF", LOG_FILE)

def motor_on(speed):
    duty = speed_map[speed]
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    log(f"Motor ON | Duty={duty}%", LOG_FILE)

def set_direction(direction):
    GPIO.output(DIR_PIN, GPIO.HIGH if direction == "F" else GPIO.LOW)
    log(f"Direction set: {direction}", LOG_FILE)

def fault_detected(channel):
    log("FAULT detected – E-STOP", LOG_FILE)
    motor_off()

GPIO.add_event_detect(
    FAULT_PIN,
    GPIO.FALLING,
    callback=fault_detected,
    bouncetime=200
)

def cleanup(signum=None, frame=None):
    log("Cleanup initiated", LOG_FILE)
    motor_off()
    pwm.stop()
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

def start_motor(speed, direction):
    log("Motor start requested", LOG_FILE)

    if not pretests_passed():
        log("Pretests NOT passed – blocking motor start", LOG_FILE)
        raise RuntimeError("Pretests failed")

    motor_off()
    time.sleep(1)

    set_direction(direction)
    time.sleep(0.5)

    motor_on(speed)

    while True:
        time.sleep(0.5)
