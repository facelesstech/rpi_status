1. Place pishutdown.py in '/home/pi/shutdown'
2. Make script executable with 'sudo chmod +x script.py'
3. Move pishutdown.service to /etc/systemd/system/
4. Enable service 'sudo systemctl enable pishutdown.service'
5. Run service at boot 'sudo systemctl start pishutdown.service'
