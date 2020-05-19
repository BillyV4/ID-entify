![alt tag](https://github.com/BillyV4/ID-entify/blob/master/Images/ID-entify-Logo.jpg)
#### By Carlos Ramírez L. | BillyV4 | V 1.0

### ABOUT
ID-entify is a tool that allows you to search for information in the passive way related to a domain.

### SEARCH FOR INFORMATION RELATED TO A DOMAIN: 
  - Emails 
  - IP addresses 
  - Subdomains 
  - Information on WEB technology 
  - Type of Firewall 
  - NS and MX records 

### THE TOOLS USED IN THE INFORMATION SEARCH ARE:
  - Fierce
  - Dnsrecon
  - Dnsenum
  - Dig
  - Blindcrawl
  - OWASP Amass
  - Nslookup
  - Whatweb
  - Wafw00f
  - Nmap http-waf-detect http-waf-fingerprint
  - Whois
  - TheHarvester
 
### TO EXECUTE THIS SCRIPT 

#### Download the script
```
git clone https://github.com/BillyV4/ID-entify.git
cd ID-entify
chmod +x id-entify.sh
```

#### Run the script
The next command is to create a workspace with tmux in which programs are executed in the background, storing the information in the ./id-domain/Raw_Data/ folder.

##### Step 1: 

```
id-entify -d google.com
```

When the programs are finished, the tmux workspace will be closed automatically, the filtered information will be stored in ./id-domain/Greep_Data/. To filter the information manually execute the following command

#### Step 2: 
```
id-entify -g google.com
```

### SCREENSHOT
#### Step 1: 

![alt tag](https://github.com/BillyV4/ID-entify/blob/master/Images/id-entify%20search.png)

#### Step 2: 
![alt tag](https://github.com/BillyV4/ID-entify/blob/master/Images/id-entify%20greep.png)
