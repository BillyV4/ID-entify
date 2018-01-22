#!/bin/bash
# Install script for ID-entify
# By BillyV4
# V 0.1
OKBLUE='\033[94m'
OKRED='\033[91m'
OKGREEN='\033[92m'
OKORANGE='\033[93m'
RESET='\e[0m'


echo -e "$OKGREEN _____ _____  $OKBLUE                       _  ___       $RESET"
echo -e "$OKGREEN(_____|____ \ $OKBLUE                  _   (_)/ __)      $RESET"
echo -e "$OKGREEN   _   _   \ \ $OKORANGE  __ $OKBLUE ____ ____ | |_  _| |__ _   _ $RESET"
echo -e "$OKGREEN  | | | |   ||$OKORANGE (___)$OKBLUE  _  )  _ \|  _)| |  __) | | |$RESET"
echo -e "$OKGREEN _| |_| |__/ /$OKBLUE     ( (/ /| | | | |__| | |  | |_| |$RESET"
echo -e "$OKGREEN(_____)_____/ $OKBLUE      \____)_| |_|\___)_|_|   \__  |$RESET"
echo -e "$OKGREEN              $OKBLUE                             (____/ $RESET"
echo -e "$OKGREEN  $RESET"
echo -e "$OKGREEN By Carlos Ramirez Lopez $RESET"
echo -e "$OKGREEN V 0.1 $RESET"
echo -e "$OKGREEN  $RESET"


INSTALL_DIR=/usr/share/ID-entify

echo -e "$OKGREEN THIS SCRIPT WILL BE INSTALLED IN $INSTALL_DIR. PRESS A KEY TO CONTINUE $RESET"
read answer 

mkdir -p $INSTALL_DIR 2> /Programs
rm -Rf $INSTALLDIR/ID-entify.py
rm -Rf $INSTALLDIR/ID-entify-report.py
cp -Rf $PWD/ID-entify.py $INSTALL_DIR
cp -Rf $PWD/ID-entify-report.py $INSTALL_DIR
cp -Rf  $PWD/Programs $INSTALL_DIR
cd $INSTALL_DIR

echo -e "$OKORANGE INSTALLING PACKAGE DEPENDENCIES...$RESET"
echo -e "$OKGREEN"

problem=$(dpkg -s dnsmap | grep installed)
 echo Checking for dnsmap : $problem
 if [ "" == "$problem" ]; then
      apt-get install dnsmap -y
 fi

problem=$(dpkg -s cewl | grep installed)
 echo Checking for cewl : $problem
 if [ "" == "$problem" ]; then
      apt-get install cewl -y
 fi

problem=$(dpkg -s theharvester | grep installed)
 echo Checking for theharvester : $problem
 if [ "" == "$problem" ]; then
      apt-get install theharvester -y
 fi

problem=$(dpkg -s dnsenum | grep installed)
 echo Checking for dnsenum : $problem
 if [ "" == "$problem" ]; then
      apt-get install dnsenum -y
 fi

problem=$(dpkg -s dnsutils | grep installed)
 echo Checking for dnsutils : $problem
 if [ "" == "$problem" ]; then
       apt-get install dnsutils -y
 fi

problem=$(dpkg -s whatweb | grep installed)
 echo Checking for whatweb : $problem
 if [ "" == "$problem" ]; then
      apt-get install whatweb -y
 fi

problem=$(dpkg -s wafw00f | grep installed)
 echo Checking for wafw00f : $problem
 if [ "" == "$problem" ]; then
      apt-get install wafw00f -y
 fi

problem=$(dpkg -s nmap | grep installed)
 echo Checking for nmap : $problem
 if [ "" == "$problem" ]; then
      atp-get install nmap -y
 fi

problem=$(dpkg -s whois | grep installed)
 echo Checking for whois : $problem
 if [ "" == "$problem" ]; then
      apt-get install whois -y
 fi

echo -e "$OKBLUE"
dpkg --get-selections | grep dnsmap
dpkg --get-selections | grep cewl
dpkg --get-selections | grep theharvester
dpkg --get-selections | grep dnsrecon
dpkg --get-selections | grep dnsenum
dpkg --get-selections | grep dnsutils
dpkg --get-selections | grep whatweb
dpkg --get-selections | grep wafw00f
dpkg --get-selections | grep nmap
dpkg --get-selections | grep  whois

echo -e ""
echo -e "$OKORANGE TO EXECUTE THIS SCRIPT $RESET"
echo -e "$OKORANGE python /usr/share/ID-entify/ID-entify.py $RESET"
echo -e ""
echo -e "$OKORANGE TO EXECUTE REPORT, NMAP AND METASPLOT $RESET"
echo -e "$OKORANGE python /usr/share/ID-entify/ID-entify-report.py $RESET"
echo -e ""
echo -e "$OKORANGE  $RESET"

