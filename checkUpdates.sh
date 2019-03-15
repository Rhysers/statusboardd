updates=$(/usr/lib/update-notifier/apt-check 2>&1)
myUpdates=(${updates//;/ })
if [[ "$updates" == "0;0" ]]
then
	python3 setLight.py 4 #No updates
elif [[ "${myUpdates[1]}" != '0' ]]
then
	python3 setLight.py 5 #Security Update
elif [[ "${myUpdates[0]}" != '0' ]]
then
	python3 setLight.py 6 #Non-Security Update
fi
if [ -f /var/run/reboot-required ]
then
	python3 setLight.py 7 #Reboot Required
fi
