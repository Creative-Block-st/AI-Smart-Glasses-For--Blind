chmod +x /home/pi/smart-glasses/startup.sh
crontab -e
@reboot /home/pi/smart-glasses/startup.sh
########################################################################################################################################################################
#!/bin/bash

# Wait for system to be fully ready
sleep 10

# Navigate to your project folder
cd /home/pi/smart-glasses

# Run the Python script
python3 smart_glasses.py
