1. Move 'wheezy_weather_screen_bmp.py' to /home/pi/
2. Edit crontab with 'EDITOR="vi" crontab -e'
3. Add this line to end of file '0,15,30,45 * * * * sudo python /home/pi/wheezy_weather_screen_bmp.py'
4. Reboot for good measure
