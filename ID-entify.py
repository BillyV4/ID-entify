# By BillyV4
# V  0.1
# -*- coding: 850 -*-
import os, sys
import subprocess
import time
from colorama import *
init(autoreset=True)

print(Style.BRIGHT + Fore.GREEN + " _____ _____  " + Style.BRIGHT + Fore.CYAN + "                       _  ___       ")
print(Style.BRIGHT + Fore.GREEN + "(_____|____ \ " + Style.BRIGHT + Fore.CYAN + "                  _   (_)/ __)      ")
print(Style.BRIGHT + Fore.GREEN + "   _   _   \ \ " + Style.BRIGHT + Fore.RED + "  __ " + Style.BRIGHT + Fore.CYAN + " ____ ____ | |_  _| |__ _   _ ")
print(Style.BRIGHT + Fore.GREEN + "  | | | |   ||" + Style.BRIGHT + Fore.RED + " (___)" + Style.BRIGHT + Fore.CYAN + "  _  )  _ \|  _)| |  __) | | |")
print(Style.BRIGHT + Fore.GREEN + " _| |_| |__/ /" + Style.BRIGHT + Fore.CYAN + "     ( (/ /| | | | |__| | |  | |_| |")
print(Style.BRIGHT + Fore.GREEN + "(_____)_____/ " + Style.BRIGHT + Fore.CYAN + "      \____)_| |_|\___)_|_|   \__  |")
print(Style.BRIGHT + Fore.GREEN + "              " + Style.BRIGHT + Fore.CYAN + "                             (____/ ")
print(Style.BRIGHT + Fore.GREEN + " By Carlos Ramirez Lopez ")
print(Style.BRIGHT + Fore.GREEN + " V0.2 ")

DOMINIO=raw_input('DOMINE: ')
PAGINA_WEB=raw_input('WEBSITE: ')

PWD_comando = "pwd | tr -d '\n'"
#print (Fore.WHITE + (PWD_comando))
PWD_resultado = subprocess.Popen(PWD_comando, shell=True, stdout=subprocess.PIPE)
for PWD_salida in PWD_resultado.stdout:
 print(PWD_salida.decode(sys.getdefaultencoding()).rstrip())

TOTAL = 12

print (Fore.WHITE + "THE FILES WILL BE SAVED IN: ")
print (Fore.WHITE + "%s/RawData/%s" % (PWD_salida, DOMINIO))

MKDIR_comando = "mkdir %s/RawData" % (PWD_salida)
MKDIR_resultado = subprocess.Popen(MKDIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

MKDIR_comando = ("mkdir %s/RawData/%s" % (PWD_salida, DOMINIO))
MKDIR_resultado = subprocess.Popen(MKDIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

time.sleep(5)

COMPLETADO = 1
print (Fore.GREEN + "Completado %s de %s" % (COMPLETADO, TOTAL))
print (Fore.YELLOW + "\nLooking for emails whit domain %s \n" % (DOMINIO))

THE_comand = ("theharvester -d %s -b all -l 999 >> %s/RawData/%s/%s_THEHARVESTER.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO))
print (Fore.WHITE + (THE_comand))
THEHARVESTER_proceso=subprocess.Popen(THE_comand, shell=True)
for num in range(1):
    print (Fore.WHITE + "Running THEHARVESTER in the background")

COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
print (Fore.YELLOW + "\nLooking for DNS and MX NS records\n")


FIERCE_comand = ("fierce -dns %s > %s/RawData/%s/%s_FIERCE.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO))
print (Fore.WHITE + (FIERCE_comand))
DNSMAP_proceso=subprocess.Popen(FIERCE_comand, shell=True)
for num in range(1):
    print (Fore.WHITE + "Running FIERCE in the background")

COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
DNSRECON_comando = "dnsrecon -z -d %s >> %s/RawData/%s/%s_DNSRECON.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (DNSRECON_comando))
DNSRECON_resultado = subprocess.Popen(DNSRECON_comando, shell=True, stdout=subprocess.PIPE)
for DNSRECON_salida in DNSRECON_resultado.stdout:
 print(DNSRECON_salida.decode(sys.getdefaultencoding()).rstrip())
 
COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
DNSENUM_comando = "dnsenum -f /usr/share/brutex/wordlists/namelist.txt %s >> %s/RawData/%s/%s_DNSENUM.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (DNSENUM_comando))
DNSENUM_resultado = subprocess.Popen(DNSENUM_comando, shell=True, stdout=subprocess.PIPE)
for DNSENUM_salida in DNSENUM_resultado.stdout:
 print(DNSENUM_salida.decode(sys.getdefaultencoding()).rstrip())
 
COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
DIG_comando = "dig %s >> %s/RawData/%s/%s_DIG.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (DIG_comando))
DIG_resultado = subprocess.Popen(DIG_comando, shell=True, stdout=subprocess.PIPE)
for DIG_salida in DIG_resultado.stdout:
 print(DIG_salida.decode(sys.getdefaultencoding()).rstrip())
 
COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
BLINDCRAWL_comando = "perl %s/Programs/blindcrawl.pl -d %s >> %s/RawData/%s/%s_BLINDCRAWL.txt" % (PWD_salida, DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (BLINDCRAWL_comando))
BLINDCRAWL_resultado = subprocess.Popen(BLINDCRAWL_comando, shell=True, stdout=subprocess.PIPE)
for BLINDCRAWL_salida in BLINDCRAWL_resultado.stdout:
 print(BLINDCRAWL_salida.decode(sys.getdefaultencoding()).rstrip())
 
COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
NSLOOKUP_comando = "nslookup -type=ns %s >> %s/RawData/%s/%s_NSLOOKUP_MX_NS.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (NSLOOKUP_comando))
NSLOOKUP_resultado = subprocess.Popen(NSLOOKUP_comando, shell=True, stdout=subprocess.PIPE)
for NSLOOKUP_salida in NSLOOKUP_resultado.stdout:
 print(NSLOOKUP_salida.decode(sys.getdefaultencoding()).rstrip())
 
NSLOOKUP_comando = "nslookup -type=mx %s >> %s/RawData/%s/%s_NSLOOKUP_MX_NS.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (NSLOOKUP_comando))
NSLOOKUP_resultado = subprocess.Popen(NSLOOKUP_comando, shell=True, stdout=subprocess.PIPE)
for NSLOOKUP_salida in NSLOOKUP_resultado.stdout:
 print(NSLOOKUP_salida.decode(sys.getdefaultencoding()).rstrip())

print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
print (Fore.YELLOW + "\nGetting web information WEB\n")

COMPLETADO = COMPLETADO + 1
WHATWEB_comando = "whatweb -a 3 -v %s >> %s/RawData/%s/%s_WHATWEB.txt" % (PAGINA_WEB, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (WHATWEB_comando))
WHATWEB_resultado = subprocess.Popen(WHATWEB_comando, shell=True, stdout=subprocess.PIPE)
for WHATWEB_salida in WHATWEB_resultado.stdout:
 print(WHATWEB_salida.decode(sys.getdefaultencoding()).rstrip())
 
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
print (Fore.YELLOW + "\nVerifying WAF\n")

COMPLETADO = COMPLETADO + 1
WAFW00F_comando = "wafw00f %s >> %s/RawData/%s/%s_WAFW00F.txt" % (PAGINA_WEB, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (WAFW00F_comando))
WAFW00F_resultado = subprocess.Popen(WAFW00F_comando, shell=True, stdout=subprocess.PIPE)
for WAFW00F_salida in WAFW00F_resultado.stdout:
 print(WAFW00F_salida.decode(sys.getdefaultencoding()).rstrip())

COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
NMAP_WAF_comando = "nmap -p 80,443 --script=http-waf-detect %s >> %s/RawData/%s/%s_NMAMP_WAF.txt" % (PAGINA_WEB, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (NMAP_WAF_comando))
NMAP_WAF_resultado = subprocess.Popen(NMAP_WAF_comando, shell=True, stdout=subprocess.PIPE)
for NMAP_WAF_salida in NMAP_WAF_resultado.stdout:
 print(NMAP_WAF_salida.decode(sys.getdefaultencoding()).rstrip())
 
NMAP_WAF_comando = "nmap -p 80,443 --script=http-waf-fingerprint %s >> %s/RawData/%s/%s_NMAMP_WAF.txt" % (PAGINA_WEB, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (NMAP_WAF_comando))
NMAP_WAF_resultado = subprocess.Popen(NMAP_WAF_comando, shell=True, stdout=subprocess.PIPE)
for NMAP_WAF_salida in NMAP_WAF_resultado.stdout:
 print(NMAP_WAF_salida.decode(sys.getdefaultencoding()).rstrip())

print (Fore.YELLOW + "\nVerifying Whois\n")

COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
WHOIS_comando = "whois %s >> %s/RawData/%s/%s_WHOIS.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (WHOIS_comando))
WHOIS_resultado = subprocess.Popen(WHOIS_comando, shell=True, stdout=subprocess.PIPE)
for WHOIS_salida in WHOIS_resultado.stdout:
 print(WHOIS_salida.decode(sys.getdefaultencoding()).rstrip())

Continuar="0\n"
print"Waiting for programs in the background, one moment",


while Continuar == "0\n":
   time.sleep(20)
   Correos = ("wc -l %s/RawData/%s/%s_FIERCE.txt | cut -d ' ' -f1" % (PWD_salida, DOMINIO, DOMINIO))
   Continuar = os.popen(Correos).read()
   print ".",
print("Report")



COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "COMPLETED SCRIPT %s de %s" % (COMPLETADO, TOTAL))

import os, sys
import subprocess
import time

print ("Domain: %s" % DOMINIO);

print(Style.BRIGHT + Fore.GREEN + " _____ _____  " + Style.BRIGHT + Fore.CYAN + "                       _  ___       ")
print(Style.BRIGHT + Fore.GREEN + "(_____|____ \ " + Style.BRIGHT + Fore.CYAN + "                  _   (_)/ __)      ")
print(Style.BRIGHT + Fore.GREEN + "   _   _   \ \ " + Style.BRIGHT + Fore.RED + "  __ " + Style.BRIGHT + Fore.CYAN + " ____ ____ | |_  _| |__ _   _ ")
print(Style.BRIGHT + Fore.GREEN + "  | | | |   ||" + Style.BRIGHT + Fore.RED + " (___)" + Style.BRIGHT + Fore.CYAN + "  _  )  _ \|  _)| |  __) | | |")
print(Style.BRIGHT + Fore.GREEN + " _| |_| |__/ /" + Style.BRIGHT + Fore.CYAN + "     ( (/ /| | | | |__| | |  | |_| |")
print(Style.BRIGHT + Fore.GREEN + "(_____)_____/ " + Style.BRIGHT + Fore.CYAN + "      \____)_| |_|\___)_|_|   \__  |")
print(Style.BRIGHT + Fore.GREEN + "              " + Style.BRIGHT + Fore.CYAN + "                             (____/ ")
print(Style.BRIGHT + Fore.GREEN + " By Carlos Ramirez Lopez ")
print(Style.BRIGHT + Fore.GREEN + " V0.2 ")


PWD_comando = "pwd | tr -d '\n'"
#print (Fore.WHITE + (PWD_comando))
PWD_resultado = subprocess.Popen(PWD_comando, shell=True, stdout=subprocess.PIPE)
for PWD_salida1 in PWD_resultado.stdout:
 print(PWD_salida1.decode(sys.getdefaultencoding()).rstrip())

COM = "'"
PWD_entrada = ("%s/RawData/%s" % (PWD_salida1, DOMINIO))
PWD_salida = ("%s/Information/%s" % (PWD_salida1, DOMINIO))
PWD_meta = ("%s/Programs" % (PWD_salida1))
PWD_NMAP = ("%s/NMAP/%s" % (PWD_salida1, DOMINIO))


DIR_comando = ("mkdir %s/Information" % (PWD_salida1))
MKDIR_resultado = subprocess.Popen(DIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

DIR_comando = ("mkdir %s/Information/%s" % (PWD_salida1, DOMINIO))
MKDIR_resultado = subprocess.Popen(DIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())


REDUCCION_DE_DOMINIO1 = ("echo '%s' > %s/Objetiv.txt" % (DOMINIO, PWD_salida))
REDUCCION_DNS = os.popen(REDUCCION_DE_DOMINIO1).read()

time.sleep(3)

REDUCCION_DE_DOMINIO2 = ("cat %s/Objetiv*.txt | cut -d '.' -f1 > %s/Objetivo.txt" % (PWD_salida, PWD_salida))
REDUCCION_DNS = os.popen(REDUCCION_DE_DOMINIO2).read()

time.sleep(3)

REDUCCION_DE_DOMINIO3 = ("rm %s/Objetiv.txt" % (PWD_salida))
REDUCCION_DNS = os.popen(REDUCCION_DE_DOMINIO3).read()

OBJETIVO_COM = ("cat %s/Objetivo*.txt" % (PWD_salida))
OBJETIVO = os.system(OBJETIVO_COM)


THEHARVESTER = ("grep -E '\@%s' %s/%s_THEHARVESTER.txt >> %s/Correos_electronicos.txt" % (DOMINIO, PWD_entrada, DOMINIO, PWD_salida))
THEHARVESTER_salida = os.popen(THEHARVESTER).read()

THEHARVESTER_DNS = ("grep -E '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' %s/%s_THEHARVESTER.txt | cut -f2 | cut -d ':' -f1 >> %s/DNS.txt" % (PWD_entrada, DOMINIO, PWD_salida))
THEHARVESTER_DNS_salida = os.popen(THEHARVESTER_DNS).read()

FIERCE_DNS = ("grep -E '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' %s/%s_FIERCE.txt | grep -v 'hostname' | cut -f2 | cut -d ':' -f1 >> %s/DNS.txt" % (PWD_entrada, DOMINIO, PWD_salida))
FIERCE_DNS_salida = os.popen(FIERCE_DNS).read()

DNSRECON = ("grep -E 'A.%s' %s/%s_DNSRECON.txt | sort -u | grep -oE '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' >> %s/IP.txt" % (DOMINIO, PWD_entrada, DOMINIO, PWD_salida))
DNSRECON_salida = os.popen(DNSRECON).read()

DNSRECON_NS_MX = ("grep -E 'NS ' %s/%s_DNSRECON.txt | sort -u | cut -d '*' -f3,4,5 -d ' ' | cut -d ' ' -f2 | grep -v 'found' | grep -v 'server' | grep -v 'duplicate' | grep -v 'Records' | grep -v '\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b' >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
DNSRECON_NS_MX_salida = os.popen(DNSRECON_NS_MX).read()

DNSRECON_NS_MX = ("grep -E 'MX ' %s/%s_DNSRECON.txt | sort -u | cut -d '*' -f3,4,5 -d ' ' | cut -d ' ' -f2 >> %s/NS_MX.txt" % (PWD_entrada, DOMINIO, PWD_salida))
DNSRECON_NS_MX_salida = os.popen(DNSRECON_NS_MX).read()

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

NS_MX = ("cat %s/NS_MX.txt | grep -v '=' | grep -v 'duplicate' | grep -v 'found:' | grep -v 'Records' | grep -v 'server' | sort -u > %s/NS_MX1.txt" % (PWD_salida, PWD_salida))
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


import subprocess
import time
from colorama import Fore, init
from numpy import array
init()

Num_salida =[0,0,0,0,0,0]

COM = "'"
PWD_entrada = ("%s/RawData/%s" % (PWD_salida1, DOMINIO))
PWD_salida = ("%s/Information/%s" % (PWD_salida1, DOMINIO))
PWD_meta = ("%s/Programs" % (PWD_salida1))
PWD_NMAP = ("%s/NMAP/%s" % (PWD_salida1, DOMINIO))


INFORMACION = ("cp -r %s/HTML/* %s/" % (PWD_meta, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()

EMAIL_Num = ("wc -l %s/Correos_electronicos.txt | cut -d' ' -f1 | tr -d '\n'" % (PWD_salida))
Num_salida[1] = os.popen(EMAIL_Num).read()

DNS_Num = ("wc -l %s/DNS.txt | cut -d' ' -f1 | tr -d '\n'" % (PWD_salida))
Num_salida[2] = os.popen(DNS_Num).read()

Informacion_WEB_Num = ("wc -l %s/Informacion_WEB.txt | cut -d' ' -f1 | tr -d '\n'" % (PWD_salida))
Num_salida[3] = os.popen(Informacion_WEB_Num).read()

NS_MX_Num = ("wc -l %s/NS_MX.txt | cut -d' ' -f1 | tr -d '\n'" % (PWD_salida))
Num_salida[4] = os.popen(NS_MX_Num).read()



Var_Mayor = 1
for x in range(0, 5, 1):
	if int(Var_Mayor) < int(Num_salida[x]):
		Var_Mayor = Num_salida [x]

Num_salida[1] = ((int(Num_salida[1]) * 100) / int(Var_Mayor))
Num_salida[2] = ((int(Num_salida[2]) * 100) / int(Var_Mayor))
Num_salida[3] = ((int(Num_salida[3]) * 100) / int(Var_Mayor))
Num_salida[4] = ((int(Num_salida[4]) * 100) / int(Var_Mayor))

INFORMACION = ("sed 's/<!--E-MAILS-->/%s/g' %s/Reporte.html > %s/Reporte_2.html" % (Num_salida[1], PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("sed 's/<!--DNS-->/%s/g' %s/Reporte_2.html > %s/Reporte_3.html" % (Num_salida[2], PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("sed 's/<!--INFORMATION-->/%s/g' %s/Reporte_3.html > %s/Reporte_4.html" % (Num_salida[3], PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("sed 's/<!--MX-->/%s/g' %s/Reporte_4.html > %s/Reporte_5.html" % (Num_salida[4], PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("sed 's/<!--DOMINIO-->/%s/g' %s/Reporte_5.html > %s/Reporte_6.html" % (DOMINIO, PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()
INFORMACION = ("sed 's/<!--OBJETIVO-->/%s/g' %s/Reporte_6.html > %s/Reporte.html" % (DOMINIO, PWD_salida, PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()

INFORMACION = ("rm %s/Reporte_*.html" % (PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()

print(Style.BRIGHT + Fore.GREEN + "Report: %s/%s/Report.html" % (PWD_salida, DOMINIO))

INFORMACION = ("firefox %s/Reporte.html" % (PWD_salida))
INFORMACION_salida = os.popen(INFORMACION).read()

print(Style.BRIGHT + Fore.GREEN + "Finish")
