
chmod +x /home/pi/robot_core/estop_daemon.py
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

sudo systemctl enable estop.service
sudo systemctl start estop.service

#run all below to make estop active
Morning
sudo systemctl start estop.service   # auto anyway
python3 launcher_release.py

End of day
sudo shutdown now

sudo systemctl status estop.service
tail -f /home/pi/logs/estop.log

ROBOT-1 DAILY START
☐ Battery connected
☐ E-stop released
☐ Pre-tests passed
☐ Area clear
☐ Start launcher

EMERGENCY
☐ Press E-stop
☐ Wait for motors to stop
☐ Investigate logs

