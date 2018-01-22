# By BillyV4
# V 0.1
# -*- coding: 850 -*-
import os, sys
import subprocess
import time
from colorama import Fore, init
init()

DOMINIO=raw_input('What is the Domine (example.com): ')
print ("Domain: %s" % DOMINIO);


print(Fore.GREEN + " _____ _____  " + Fore.CYAN + "                       _  ___       ")
print(Fore.GREEN + "(_____|____ \ " + Fore.CYAN + "                  _   (_)/ __)      ")
print(Fore.GREEN + "   _   _   \ \ " + Fore.RED + "  __ " + Fore.CYAN + " ____ ____ | |_  _| |__ _   _ ")
print(Fore.GREEN + "  | | | |   ||" + Fore.RED + " (___)" + Fore.CYAN + "  _  )  _ \|  _)| |  __) | | |")
print(Fore.GREEN + " _| |_| |__/ /" + Fore.CYAN + "     ( (/ /| | | | |__| | |  | |_| |")
print(Fore.GREEN + "(_____)_____/ " + Fore.CYAN + "      \____)_| |_|\___)_|_|   \__  |")
print(Fore.GREEN + "              " + Fore.CYAN + "                             (____/ ")
print(Fore.GREEN + " By Carlos Ramirez Lopez")
print(Fore.GREEN + " V0.1 ")


COM = "'"
PWD_entrada = ("/usr/share/ID-entify/RawData/%s" % (DOMINIO))
PWD_salida = ("/usr/share/ID-entify/Information/%s" % (DOMINIO))
PWD_meta = "/usr/share/ID-entify/Programs"
PWD_NMAP = ("/usr/share/ID-entify/NMAP/%s" % (DOMINIO))


POSTGRESQL_comando = "service postgresql start"
MKDIR_resultado = subprocess.Popen(POSTGRESQL_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

DIR_comando = "mkdir /usr/share/ID-entify/Information"
MKDIR_resultado = subprocess.Popen(DIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

DIR_comando = ("mkdir /usr/share/ID-entify/Information/%s" % (DOMINIO))
MKDIR_resultado = subprocess.Popen(DIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

MKDIR_comando = "mkdir /usr/share/ID-entify/NMAP"
MKDIR_resultado = subprocess.Popen(MKDIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

MKDIR_comando = ("mkdir /usr/share/ID-entify/NMAP/%s" % (DOMINIO))
MKDIR_resultado = subprocess.Popen(MKDIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

REDUCCION_DE_DOMINIO1 = ("echo '%s' > %s/Objetiv.txt" % (DOMINIO, PWD_salida))
REDUCCION_DNS = os.popen(REDUCCION_DE_DOMINIO1).read()

time.sleep(2)

REDUCCION_DE_DOMINIO2 = ("cat %s/Objetiv*.txt | cut -d '.' -f1 > %s/Objetivo.txt" % (PWD_salida, PWD_salida))
REDUCCION_DNS = os.popen(REDUCCION_DE_DOMINIO2).read()

time.sleep(2)

REDUCCION_DE_DOMINIO3 = ("rm %s/Objetiv.txt" % (PWD_salida))
REDUCCION_DNS = os.popen(REDUCCION_DE_DOMINIO3).read()

OBJETIVO_COM = ("cat %s/Objetivo*.txt" % (PWD_salida))
OBJETIVO = os.system(OBJETIVO_COM)


NMAP_Pregunta=raw_input(Fore.YELLOW + ("Do you want to run nmapdo you want to run NMAP?\n 1 = SI\n 2 = NO\n"))

THEHARVESTER = ("grep -E '\@%s' %s/%s_THEHARVESTER.txt >> %s/Correos_electronicos.txt" % (DOMINIO, PWD_entrada, DOMINIO, PWD_salida))
THEHARVESTER_salida = os.popen(THEHARVESTER).read()

THEHARVESTER_DNS = ("grep -E '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' %s/%s_THEHARVESTER.txt | cut -f2 | cut -d ':' -f1 >> %s/DNS.txt" % (PWD_entrada, DOMINIO, PWD_salida))
THEHARVESTER_DNS_salida = os.popen(THEHARVESTER_DNS).read()

DNSMAP = ("grep '%s' %s/%s_DNSMAP.txt | cut -d ':' -f1 -d ' ' | grep '%s'>> %s/DNS.txt" % (OBJETIVO, PWD_entrada, DOMINIO, PWD_salida, DOMINIO))
DNSMAP_salida = os.popen(DNSMAP).read()

DNSRECON = ("grep -E 'A.%s' %s/%s_DNSRECON.txt | sort -u | grep -oE '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' >> %s/IP.txt" % (DOMINIO, PWD_entrada, DOMINIO, PWD_salida))
DNSRECON_salida = os.popen(DNSRECON).read()

DNSRECON_NS_MX = ("grep -E 'NS ' %s/%s_DNSRECON.txt | sort -u | cut -d '*' -f3,4,5 -d ' ' | cut -d ' ' -f2 >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
DNSRECON_NS_MX_salida = os.popen(DNSRECON_NS_MX).read()

DNSRECON_NS_MX = ("grep -E 'MX ' %s/%s_DNSRECON.txt | sort -u | cut -d '*' -f3,4,5 -d ' ' | cut -d ' ' -f2 >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
DNSRECON_NS_MX_salida = os.popen(DNSRECON_NS_MX).read()

# DNSENUM = ("grep -E 'IN ' %s/%s_DNSENUM.txt | grep -E 'mx' | cut -d ' ' -f1 >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
# DNSENUM_salida = os.popen(DNSENUM).read()

# DNSENUM = ("grep -E 'IN ' %s/%s_DNSENUM.txt | grep -E 'ns' | cut -d ' ' -f1 >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
# DNSENUM_salida = os.popen(DNSENUM).read()

BLINDCRAWL = ("grep '\.%s' %s/%s_BLINDCRAWL.txt | cut -d ':' -f1 -d ' ' >> %s/DNS.txt" % (DOMINIO, PWD_entrada, DOMINIO, PWD_salida))
BLINDCRAWL_salida = os.popen(BLINDCRAWL).read()

NSLOOKUP = ("grep -E ' = ' %s/%s_NSLOOKUP_MX_NS.txt | grep 'mx' | cut -d ' ' -f3 >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
NSLOOKUP_salida = os.popen(NSLOOKUP).read()

NSLOOKUP = ("grep -E ' = ' %s/%s_NSLOOKUP_MX_NS.txt | grep 'mx' | cut -d ' ' -f5 >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
NSLOOKUP_salida = os.popen(NSLOOKUP).read()

WHATWEB = ("grep -E ']' %s/%s_WHATWEB.txt >> %s/Informacion_WEB.txt" % (PWD_entrada, DOMINIO, PWD_salida))
WHATWEB_salida = os.popen(WHATWEB).read()

WAFWOOF = ("grep -E 'site' %s/%s_WAFW00F.txt  >> %s/WAF.txt" % (PWD_entrada, DOMINIO, PWD_salida))
WAFWOOF_salida = os.popen(WAFWOOF).read()

NMAP = ("grep -E '_' %s/%s_NMAMP_WAF.txt >> %s/WAF.txt" % (PWD_entrada, DOMINIO, PWD_salida))
NMAP_salida = os.popen(NMAP).read()

WHOIS = ("cat %s/%s_WHOIS.txt >> %s/WHOIS.txt" % (PWD_entrada, DOMINIO, PWD_salida))
WHOIS_salida = os.popen(WHOIS).read()

Correos = ("cat %s/Correos_electronicos.txt | sort -u > %s/Correos_electronicos1.txt" % (PWD_salida, PWD_salida))
Correos_salida = os.popen(Correos).read()
Correos = ("rm %s/Correos_electronicos.txt" % (PWD_salida))
Correos_salida = os.popen(Correos).read()
Correos = ("cp %s/Correos_electronicos1.txt %s/Correos_electronicos.txt" % (PWD_salida, PWD_salida))
Correos_salida = os.popen(Correos).read()
Correos = ("rm %s/Correos_electronicos1.txt" % (PWD_salida))
Correos_salida = os.popen(Correos).read()

DNS = ("cat %s/DNS*.txt | sort -u > %s/DNS1.txt" % (PWD_salida, PWD_salida))
DNS_salida = os.popen(DNS).read()
DNS = ("rm %s/DNS.txt" % (PWD_salida))
DNS_salida = os.popen(DNS).read()
DNS = ("cp %s/DNS1.txt %s/DNS.txt" % (PWD_salida, PWD_salida))
DNS_salida = os.popen(DNS).read()
DNS = ("rm %s/DNS1.txt" % (PWD_salida))
DNS_salida = os.popen(DNS).read()

INFORMACION = ("cat %s/Informacion_WEB.txt | sort -u > %s/Informacion_WEB1.txt" % (PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("rm %s/Informacion_WEB.txt" % (PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("cp %s/Informacion_WEB1.txt %s/Informacion_WEB.txt" % (PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("rm %s/Informacion_WEB1.txt" % (PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()

NS_MX = ("cat %s/NS_MX.txt | cut -d ' ' -f1 | sort -u > %s/NS_MX1.txt" % (PWD_salida, PWD_salida))
NS_MX_salida = os.popen(NS_MX).read()
NS_MX = ("rm %s/NS_MX.txt" % (PWD_salida))
NS_MX_salida = os.popen(NS_MX).read()
NS_MX = ("cp %s/NS_MX1.txt %s/NS_MX.txt" % (PWD_salida, PWD_salida))
NS_MX_salida = os.popen(NS_MX).read()
NS_MX = ("rm %s/NS_MX1.txt" % (PWD_salida))
NS_MX_salida = os.popen(NS_MX).read()

IP = ("cat %s/IP.txt | sort -u > %s/IP1.txt" % (PWD_salida, PWD_salida))
IP_salida = os.popen(IP).read()
IP = ("rm %s/IP.txt" % (PWD_salida))
IP_salida = os.popen(IP).read()
IP = ("cp %s/IP1.txt %s/IP.txt" % (PWD_salida, PWD_salida))
IP_salida = os.popen(IP).read()
IP = ("rm %s/IP1.txt" % (PWD_salida))
IP_salida = os.popen(IP).read()

print(Fore.YELLOW + "%s results whith IP address:" % DOMINIO)
print(Fore.WHITE + "")

IP_ARCHIVO = ("cat %s/IP.txt" % (PWD_salida))
IP_ARCHIVO_valor = os.system(IP_ARCHIVO)
print(Fore.WHITE + "")

print(Fore.YELLOW + "Information WEB:")
print(Fore.WHITE + "")

WEB_ARCHIVO = ("cat %s/Informacion_WEB.txt" % (PWD_salida))
WEB_ARCHIVO_valor = os.system(WEB_ARCHIVO)
print(Fore.WHITE + "")

print(Fore.YELLOW + "Records NS y MX:")
print(Fore.WHITE + "")

NS_MX_ARCHIVO = ("cat %s/NS_MX.txt" % (PWD_salida))
NS_MX_ARCHIVO_valor = os.system(NS_MX_ARCHIVO)
print(Fore.WHITE + "")

print(Fore.YELLOW + "Information WAF")
print(Fore.WHITE + "")

WAF_ARCHIVO = ("cat %s/WAF.txt" % (PWD_salida))
WAF_ARCHIVO_valor = os.system(WAF_ARCHIVO)
print(Fore.WHITE + "")

print(Fore.YELLOW + "Directions found:")
print(Fore.WHITE + "")

DNS_ARCHIVO = ("cat %s/DNS*.txt" % (PWD_salida))
DNS_ARCHIVO_valor = os.system(DNS_ARCHIVO)
print(Fore.WHITE + "")


if NMAP_Pregunta == "1":
 print(Fore.YELLOW + "Importing database to METASPLOIT")

 Eye_comando = ("python /usr/share/ID-entify/Programs/EyeWitness.py -f /usr/share/ID-entify/Programs/Information/DNS.txt --web")
 print (Fore.WHITE + (Eye_comando))
 Eye_resultado = subprocess.Popen(Eye_comando, shell=True, stdout=subprocess.PIPE)
 for Eye_salida in Eye_resultado.stdout:
  print(Eye_salida.decode(sys.getdefaultencoding()).rstrip())
print "FIN"


if NMAP_Pregunta == "1":
 print(Fore.YELLOW + "Running NMAP:")

 NMAP_comando = ("nmap -vvv -sS -Pn -sV -T3 -p 21,22,23,25,58,79,80,110,111,135,139,161,389,443,445,512,513,687,879,1433,1434,1521,1556,1971,2148,3389,4145,4343,4888,5053,5400,5500,5600,5601,5634,5700,5800,8080,8081 --open -oA %s/nmap%s -iL %s/DNS*.txt" % (PWD_NMAP, DOMINIO, PWD_salida))
 print (Fore.WHITE + (NMAP_comando))
 NMAP_resultado = subprocess.Popen(NMAP_comando, shell=True, stdout=subprocess.PIPE)
 for NMAP_salida in NMAP_resultado.stdout:
  print(NMAP_salida.decode(sys.getdefaultencoding()).rstrip())
 
 ECH_ARCHIVO = ("echo 'workspace -a %s_ID_entify \nworkspace %s_ID_entify\ndb_import /usr/share/ID-entify/NMAP/%s/nmap%s.xml\nservices -S filtered -d\nservices -S closed -d\nuse auxiliary/scanner/ftp/anonymous\nservices -p 21 -R\nset FTPPASS anonymous\nrun\nunset FTPPASS%s%s\nrun\nuse auxiliary/scanner/http/options\nservices -p 80 -R\nrun\nexit\n' > %s/metasploit.txt" % (DOMINIO, DOMINIO, DOMINIO, DOMINIO, COM, COM, PWD_meta))
 ECH_ARCHIVO_valor = os.system(ECH_ARCHIVO)
 print(Fore.WHITE + "")

if NMAP_Pregunta == "1":
 print(Fore.YELLOW + "Importing database to METASPLOIT")

 META_comando = ("msfconsole -r /usr/share/ID-entify/Programs/metasploit.txt")
 print (Fore.WHITE + (META_comando))
 META_resultado = subprocess.Popen(META_comando, shell=True, stdout=subprocess.PIPE)
 for META_salida in META_resultado.stdout:
  print(META_salida.decode(sys.getdefaultencoding()).rstrip())
print "Finish"
