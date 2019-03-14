#!/bin/bash

debugging="True"

if [ -z $1 ]
then
    echo -e "Usage: checkport [port number]"
    exit
else
    IP_ADDRESS=$(curl --silent ifconfig.me/ip) > /dev/null
    RESULT=$(curl --silent --data "port=$1&IP=$IP_ADDRESS" https://www.canyouseeme.org |grep Success)

    if [[ -z $RESULT ]]
    then
        if [[ $debugging == "True" ]]
        then
            echo -e "The port $1 is NOT open!"
        fi
        ping -c 2 8.8.4.4 > /dev/null
        rc=$?
        if [[ $rc -eq 0 ]]
        then
            if [[ $debugging == "True" ]]
            then
                echo "Can Reach Google"
            fi
            python3 setLight.py 2
        else
            if [[ $debugging == "True" ]]
            then
                echo "Can't Reach Google"
            fi
            python3 setLight.py 3
        fi
    else
        if [[ $debugging == "True" ]]
        then
            echo -e "The port $1 IS open!"
        fi
        python3 setLight.py 1
    fi
fi

