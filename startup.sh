#!/bin/bash

sleep 15
/etc/statusboardd/check-accessibility.sh 443
sleep 2
/etc/statusboardd/checkUpdates.sh
