#!/bin/bash
source=~/.bash_profile
while true; do
	echo "Starting"
	/usr/bin/python main.py
	echo "Exited... waiting to restart"
	sleep 4
done
