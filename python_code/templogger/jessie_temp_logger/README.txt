1. Move templogger.py to /home/pi/
2. Move templogger.service templogger.timer to /etc/systemd/system/
3. Enable service 'sudo systemctl enable templogger.timer'
4. Run service at boot 'sudo systemctl start templogger.timer'
