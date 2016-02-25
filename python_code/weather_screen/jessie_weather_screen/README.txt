1. Move 'jessie_weather_screen.py' to /home/pi/
2. Move both weather_screen.service and weather_screen.timer to /etc/systemd/system/
3. Enable it with 'sudo systemctl enable weather_screen.timer'
4. Start at boot with 'sudo systemctl start weather_screen.timer'
5. Reboot when done
