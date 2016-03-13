1. Move templogger.py to /home/pi/
2. Make script executable with 'sudo chmod +x script.py'
3. Edit crontab with 'EDITOR="vi" crontab -e'
4. Add this line to end of file '0,15,30,45 * * * * sudo python /home/pi/templogger.py'
5. Reboot for good measure
