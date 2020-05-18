#!/bin/bash

# Author: BllyV4 Carlos Ramirez L.
# Version: 1.0
# Colours
greenC="\e[0;32m\033[1m"
endC="\033[0m\e[0m"
redC="\e[0;31m\033[1m"
blueC="\e[0;34m\033[1m"
yellowC="\e[0;33m\033[1m"
purpleC="\e[0;35m\033[1m"
turquoiseC="\e[0;36m\033[1m"
grayC="\e[0;37m\033[1m"

VERSION="1.0"
TIMER="sleep 1"
LONG_TIMER="tmux send-keys 'sleep 8.0' C-m"

export DEBIAN_FRONTEND=noninteractive


echo -e "${greenC} _____ _____  ${blueC}                       _  ___       "
echo -e "${greenC}(_____|____ \ ${blueC}                  _   (_)/ __)      "
echo -e "${greenC}   _   _   \ \ ${redC}  __ ${blueC} ____ ____ | |_  _| |__ _   _ "
echo -e "${greenC}  | | | |   ||${redC} (___)${blueC}  _  )  _ \|  _)| |  __) | | |"
echo -e "${greenC} _| |_| |__/ /${blueC}     ( (/ /| | | | |__| | |  | |_| |"
echo -e "${greenC}(_____)_____/ ${blueC}      \____)_| |_|\___)_|_|   \__  |"
echo -e "${greenC}              ${blueC}                             (____/ "
echo -e "${yellowC} By BillyV4 | Carlos Ramirez L "
echo -e "${yellowC} Version 1.0 ${endC}\n"

trap ctrl_c INT


function ctrl_c(){
	tmux kill-session -t id-entify
	echo -e "\n **** ${redC}Temux session deleted${endC} **** \n"
	exit 0
}

function helpPanel(){
	echo -e "\n**** Options: ****\n"
	echo -e "\t-d\tspecify the domain"
	echo -e "\t-g\tGreep raw data"
	echo -e "\t-u\tCheck updates"

	echo -e "\n**** View result - Tmux pannel ****\n"
	echo -e "tmux list-sessions"
	echo -e "tmux attach -t id-entify"
	echo -e "tmux kill-session -t id-entify"

	echo -e "\n**** Example ****\n"
	echo -e "Step 1: id-entify -d google.com"
	echo -e "Step 2: id-entify -g google.com\n"

	exit 0
}

function startUpdate(){

		OnlineVersion=$(curl -s https://raw.githubusercontent.com/BillyV4/ID-entify/master/ID-entify.py | grep "# Version" | cut -d " " -f3)
		if [[ $OnlineVersion == $VERSION ]]; then
			echo -e "\n${greenC}id-entify is updated to the latest version :)${endC}\n" 

		else
			echo -e "\n${purpleC}A new version is now available ${endC} \n"

		fi

		exit 0
}


function startGreep(){
		
		echo -e "\nFiltering the following ${greenC}$DOMAIN${endC} domain files \n\nExtracting files from: ${greenC}./id-$DOMAIN/Raw_Data/${endC}"
		for Files in $(ls ./id-$DOMAIN/Raw_Data/); do echo -e -n "\n${greenC} [*] ${endC} "; echo -n $Files; done; echo -e "\n"
		echo -e "Filter files stored in: ${greenC}./id-$DOMAIN/Grep_Data/:${endC}"

		#---------------------------------------------------
		cat ./id-$DOMAIN/Raw_Data/fierce.txt | grep -E "\b([0-9]{1,3}.){3}[0-9]{1,3}\b" | grep -v ":" | grep -v "** Found" | sed -e 's/	/,/g' > ./id-$DOMAIN/Grep_Data/Records.txt && $TIMER
		cat ./id-$DOMAIN/Raw_Data/dnsrecon.txt | grep "	" | cut -d " " -f3,4,5,6 > ./id-$DOMAIN/Grep_Data/Records_MX_NS.txt
		cat ./id-$DOMAIN/Raw_Data/dnsenum | sed -e 's/<\/fqdn>/\n/g' | cut -d ">" -f2,6 | grep hostname | sed -e 's/<hostname>/,/g' >> ./id-$DOMAIN/Grep_Data/Records.txt
		cat ./id-$DOMAIN/Raw_Data/amass | cut -d "\"" -f4,14 | sed -e 's/\"/ /g' | awk '{ print $2 " " $1 }' | sed -e 's/ /,/g' >> ./id-$DOMAIN/Grep_Data/Records.txt
		cat ./id-$DOMAIN/Raw_Data/nslookupmx.txt  | grep "=" >> ./id-$DOMAIN/Grep_Data/Records_MX_NS.txt
		cat ./id-$DOMAIN/Raw_Data/nslookupns.txt  | grep "=" >> ./id-$DOMAIN/Grep_Data/Records_MX_NS.txt
		cat ./id-$DOMAIN/Raw_Data/dig.txt | grep "IN" | grep -E "\b([0-9]{1,3}.){3}[0-9]{1,3}\b" >> ./id-$DOMAIN/Grep_Data/IP.txt
		cat ./id-$DOMAIN/Raw_Data/blindcrawl.txt | grep -E "\b([0-9]{1,3}.){3}[0-9]{1,3}\b" | awk '{ print $2 " " $1 }' | sed -e 's/ /,/g' >> ./id-$DOMAIN/Grep_Data/Records.txt
		echo -e "\nNmap Result\n" > ./id-$DOMAIN/Grep_Data/WAF.txt
		cat ./id-$DOMAIN/Raw_Data/nmap_waf_*.txt | grep "_" >> ./id-$DOMAIN/Grep_Data/WAF.txt
		cat ./id-$DOMAIN/Raw_Data/wafw00f.txt >> ./id-$DOMAIN/Grep_Data/WAF.txt
		cp ./id-$DOMAIN/Raw_Data/whatweb.txt ./id-$DOMAIN/Grep_Data/Web.txt
		cp ./id-$DOMAIN/Raw_Data/whois.txt ./id-$DOMAIN/Grep_Data/Whois.txt
		cp ./id-$DOMAIN/Raw_Data/theharvester.txt ./id-$DOMAIN/Grep_Data/Email.txt
		sleep .5
		cat ./id-$DOMAIN/Grep_Data/Records.txt | sort -u > ./id-$DOMAIN/Grep_Data/DNS.txt
		sleep .5
		rm ./id-$DOMAIN/Grep_Data/Records.txt
		#---------------------------------------------------
		
		for Files in $(ls ./id-$DOMAIN/Grep_Data/); do echo -e -n "\n${greenC} [*] ${endC} "; echo -n $Files; done; echo -e "\n"
		for DNS_List in $(cat ./id-$DOMAIN/Grep_Data/DNS.txt); do echo -e "${yellowC} [*] ${endC} $DNS_List"; sleep .1; done; echo 




}

function startScript(){
	
	#Mkdir 

	#if [ "$(echo $DOMAIN)" != "" ] && [ "$(echo $WEB)" != "" ]; then
	if [ "$(echo $DOMAIN)" != "" ]; then

		mkdir "id-$DOMAIN" > /dev/null 2>&1
		mkdir "./id-$DOMAIN/Raw_Data" > /dev/null 2>&1
		mkdir "./id-$DOMAIN/Grep_Data" > /dev/null 2>&1
		RAW="./id-$DOMAIN/Raw_Data/$DOMAIN"
		RAW_DIR="./id-$DOMAIN/Raw_Data"
		RAW_GREP="./id-$DOMAIN/Grep_Data"

	fi

		#Commands
		whatweb="whatweb -a 3 -v $DOMAIN"
		dnsrecon="dnsrecon -z -d $DOMAIN"
		dnsenum="dnsenum -o $RAW_DIR/dnsenum $DOMAIN"
		dig="dig $DOMAIN"
		nslookupns="nslookup -type=ns $DOMAIN"
		nslookupmx="nslookup -type=mx $DOMAIN"
		wafw00f="wafw00f $DOMAIN"
		nmap_waf_detect="nmap -p 80,443 --script=http-waf-detect $DOMAIN"
		nmap_waf_finger="nmap -p 80,443 --script=http-waf-fingerprint $DOMAIN"
		whois="whois $DOMAIN"
		

		#BACKGROUD TOOLS
		theharvester="theHarvester -d $DOMAIN -b all"
		fierce="fierce -dns $DOMAIN"
		blindcrawl="perl ./Programs/blindcrawl.pl -d $DOMAIN"
		amass="amass enum -d $DOMAIN -json $RAW_DIR/amass"




	#Get Dominio

	if [ "$(echo $DOMAIN)" != "" ]; then

		#---------------------------------------------------

		tmux start-server && $TIMER
		tmux new-session -d -t "id-entify" && $TIMER
		tmux rename-window "Tools"
		echo -e "\nMaking Tmux Workspace\n"
		#Main
		for SPLIT in {1..3};do tmux split-window -h; $TIMER; done
		#Background
		tmux new-window -t id-entify:2 -n "Background" && $TIMER
		for SPLIT in {1..3};do tmux split-window -h; $TIMER; done		
		
		#---------------------------------------------------

		tmux select-pane -t 1 && $TIMER
		tmux send-keys "$theharvester > $RAW_DIR/theharvester.txt 2> Log.txt && $TIMER" C-m;
		echo -e "${greenC} [*] ${endC}" Starting TheHarvester;

		#---------------------------------------------------

		tmux select-pane -t 2 && $TIMER
		tmux send-keys "$fierce > $RAW_DIR/fierce.txt 2> Log.txt && $TIMER" C-m;
		echo -e "${greenC} [*] ${endC}" Starting Fierce;
		
		#---------------------------------------------------

		tmux select-pane -t 3 && $TIMER
		tmux send-keys "$dnsenum; $blindcrawl > $RAW_DIR/blindcrawl.txt && $TIMER" C-m;
		echo -e "${greenC} [*] ${endC}" Starting Blindcrawl;

		#---------------------------------------------------

		tmux select-pane -t 4 && $TIMER
		tmux send-keys "$amass; while [[ \$(cat ./id-$DOMAIN/Status.txt 2> /dev/null) != "111" ]]; do echo -n ". "; sleep 5; done; clear; id-entify -g $DOMAIN; echo "Id-entify has been successfully completed"; sleep 30; exit 0" C-m;
		echo -e "${greenC} [*] ${endC}" Starting OWASP Amass;
		#tmux send-keys "for Second_part in {1..2000} cat ./id-$DOMAIN/Status.txt 2> /dev/null) != "111" ]]; do echo -n ". "; sleep 5; done; clear; id-entify -g $DOMAIN; echo "Id-entify has been successfully completed"; sleep 30; exit 0" C-m;
		
		
		#---------------------------------------------------

		tmux select-window -t 1

		#---------------------------------------------------

		tmux select-pane -t 1 && $TIMER
		tmux send-keys "$whatweb > $RAW_DIR/whatweb.txt 2> Log.txt " C-m;
		echo -e "${greenC} [*] ${endC}" Starting Whatwheb;
		tmux send-keys "$dnsrecon > $RAW_DIR/dnsrecon.txt 2> Log.txt" C-m;
		echo -e "${greenC} [*] ${endC}" Starting DNSRecon;
		tmux send-keys "$dnsenum" C-m;
		echo -e "${greenC} [*] ${endC}" Starting DNSEnum;

		#---------------------------------------------------

		tmux select-pane -t 2 && $TIMER
		tmux send-keys "$dig > $RAW_DIR/dig.txt" C-m;
		tmux send-keys "$nslookupmx > $RAW_DIR/nslookupmx.txt 2> Log.txt" C-m;
		echo -e "${greenC} [*] ${endC}" Starting NSLookup MX;
		tmux send-keys "$nslookupns > $RAW_DIR/nslookupns.txt 2> Log.txt" C-m;
		echo -e "${greenC} [*] ${endC}" Starting NSLookup NS;

		#---------------------------------------------------

		tmux select-pane -t 3 && $TIMER
		tmux send-keys "$wafw00f > $RAW_DIR/wafw00f.txt 2> Log.txt" C-m;
		echo -e "${greenC} [*] ${endC}" Starting WafW00f;
		tmux send-keys "$nmap_waf_finger > $RAW_DIR/nmap_waf_finger.txt 2> Log.txt && $nmap_waf_detect > $RAW_DIR/nmap_waf_detect.txt 2> Log.txt" C-m;
		echo -e "${greenC} [*] ${endC}" Starting Nmap Waf Finger and Detect;

		#---------------------------------------------------

		tmux select-pane -t 4 && $TIMER
		tmux send-keys "$whois > $RAW_DIR/whois.txt 2> Log.txt" C-m;
		echo -e "${greenC} [*] ${endC}" Starting Whois;

		#---------------------------------------------------
		
		tmux select-window -t 2
		echo -n -e "${greenC} [*] ${endC} Wait a second.";
		rm ./id-$DOMAIN/Status.txt 2> /dev/null

			
		for Exit_Tmux in {1..3}
		do 
			echo -n " .";
			tmux select-pane -t $Exit_Tmux && $TIMER
			tmux send-keys "echo -n '1' >> ./id-$DOMAIN/Status.txt; sleep 10; exit" C-m && $TIMER;
			#tmux send-keys "echo -e 'Script $Exit_Tmux Ended'; sleep 20; echo -n '1' >> ./id-$DOMAIN/Status.txt; exit;" C-m && $TIMER;
		done
		
			tmux select-pane -t 4 && $TIMER
			#tmux send-keys "echo -n 1 >> ./id-$DOMAIN/Status.txt; exit;" C-m && $TIMER;
			tmux select-window -t 1

		for Exit_Tmux in {1..4}
		do 
			echo -n " .";
			tmux select-pane -t $Exit_Tmux && $TIMER
			tmux send-keys "echo -e " "; sleep 10; exit" C-m && $TIMER;
		done
		#---------------------------------------------------
		echo -e "\n\n${yellowC}**** Are still running in the background - Tmux session will be automatically closed when it ends ***** ${endC}\n"
		tmux list-sessions
		echo -e "\n${yellowC}******************************************************************************************************* ${endC}\n"
		echo -e "${blueC} [!] ${endC}At the end of all the processes the ${greenC} id-entify -g $DOMAIN ${endC}command will be executed. "
		echo -e "${blueC} [!] ${endC}Or you can execute it manually to filter the files that are already available."
		#---------------------------------------------------
		
		####OPEN TMUX #####
		#tmux select-window -t 1
		#tmux attach -t id-entify
		
		#---------------------------------------------------


	else
		echo "DOMINIO without parameters assigned"
	fi


	#Get WEB

	if [ "$(echo $WEB)" != "" ]; then

		echo -e ""

	else
		echo ""
	fi


}


#Main function
if [ "$(id -u)" == "0" ]; then
	declare -i parameter_counter=0; while getopts d:w:g:hu arg; do
		case $arg in
			d) DOMAIN=$OPTARG; let parameter_counter+=1 ;;
			#w) WEB=$OPTARG; let parameter_counter+=1 ;;
			g) DOMAIN=$OPTARG; let parameter_counter+=3 ;;
			u) startUpdate;;
			h) helpPanel;;
		esac
	done
	
	#Start Grep
	if [[ $parameter_counter == 3 ]]; then
		
		startGreep

	fi

	#Start Scrip
	if [ $parameter_counter == 1 ]; then
		
		startScript

	#else
		
	#	helpPanel
	fi
else
	echo -e "\n${redC}[*] You aren't root${endC}\n"
fi
