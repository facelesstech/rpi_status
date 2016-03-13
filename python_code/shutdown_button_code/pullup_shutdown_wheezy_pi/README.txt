1. Place pishutdown.py in '/home/pi/shutdown/'
2. Make script executable with 'sudo chmod +x script.py'
3. Edit '/etc/rc.local' as root aka 'sudo vi /etc/rc.local'
4. Add 'sudo python /home/pi/shutdown/pishutdown.py' before the 'exit 0' line
5. Save file and reboot pi
