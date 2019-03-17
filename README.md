# statusboardd
background process to manage lights for Status Board

Process uses Python socket library to listen on local loopback port 65432 for commands to update the lights. Run with crontab @reboot and put in background with &

Can also run the check-accessibility.sh and checkUpdates.sh scritps to check for internet access and presence of updates.
checkUpdates reqires the /usr/lib/update-notifier/ library which can be copied from Ubuntu, or I'm sure other places.
client.py can be used to manually send commands for testing.
