#!/bin/bash 
#
# Adapted from: https://matrix.senecacollege.ca/~lnx255/eap.config
#				M. Heidenreich, (c) 2019-2022
#

ssid="SenecaNET" 
read -p "Please enter your MySeneca user name (all upper case): "  user 
read -sp "Please enter your MySeneca password: "  password 

echo 
hash=$(echo -n $password | iconv -t utf16le | openssl md4 | cut -d" " -f2) 

cat << NETWORK 
network={ 
	ssid=$ssid 
	key_mgmt=WPA-EAP 
	pairwise=CCMP 
	auth_alg=OPEN 
	eap=PEAP 
	identity="$user" 
	password=hash:$hash 
	phase1="peaplabel=0" 
	phase2="auth=MSCHAPV2" 
} 
NETWORK



