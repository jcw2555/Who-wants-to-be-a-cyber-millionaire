#!/bin/bash

#check for necessary packages
packages=("python3" "mysql-server" "python3-pip" "python3-flask")

for pkg in "${packages[@]}"
do
	PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $pkg|grep "install ok installed")
	echo Checking for $pkg: $PKG_OK
	if [ "" == "$PKG_OK" ]; then
		echo "No $pkg. Setting up $pkg."
		sudo apt-get update
		sudo apt-get --force-yes --yes install $pkg
	fi
done

#run game
python3 /var/www/html/ajax_test.py
