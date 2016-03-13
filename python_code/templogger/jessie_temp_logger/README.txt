1. Move templogger.py to /home/pi/
2. Make script executable with 'sudo chmod +x script.py'
3. Move templogger.service templogger.timer to /etc/systemd/system/
4. Enable service 'sudo systemctl enable templogger.timer'
5. Run service at boot 'sudo systemctl start templogger.timer'
