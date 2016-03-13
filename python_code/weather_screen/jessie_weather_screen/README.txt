1. Move 'jessie_weather_screen.py' to /home/pi/
2. Make script executable with 'sudo chmod +x script.py'
3. Move both weather_screen.service and weather_screen.timer to /etc/systemd/system/
4. Enable it with 'sudo systemctl enable weather_screen.timer'
5. Start at boot with 'sudo systemctl start weather_screen.timer'
6. Reboot when done
