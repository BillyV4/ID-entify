# By BillyV4
# V  0.1
# -*- coding: 850 -*-
import os, sys
import subprocess
import time

from colorama import Fore, init
init()

print(Fore.GREEN + " _____ _____  " + Fore.CYAN + "                       _  ___       ")
print(Fore.GREEN + "(_____|____ \ " + Fore.CYAN + "                  _   (_)/ __)      ")
print(Fore.GREEN + "   _   _   \ \ " + Fore.RED + "  __ " + Fore.CYAN + " ____ ____ | |_  _| |__ _   _ ")
print(Fore.GREEN + "  | | | |   ||" + Fore.RED + " (___)" + Fore.CYAN + "  _  )  _ \|  _)| |  __) | | |")
print(Fore.GREEN + " _| |_| |__/ /" + Fore.CYAN + "     ( (/ /| | | | |__| | |  | |_| |")
print(Fore.GREEN + "(_____)_____/ " + Fore.CYAN + "      \____)_| |_|\___)_|_|   \__  |")
print(Fore.GREEN + "              " + Fore.CYAN + "                             (____/ ")
print(Fore.GREEN + " By Carlos Ramirez Lopez ")
print(Fore.GREEN + " V0.1 ")

DOMINIO=raw_input('WHAT IS THE DOMINE?: ')
print ("Domine: %s" % DOMINIO);

PAGINA_WEB=raw_input('WHICH IS THE WEBSITE?: ')
print ("Website: %s" % PAGINA_WEB);

PWD_salida = "/usr/share/ID-entify"
TOTAL = 12

print (Fore.WHITE + "THE FILES WILL BE SAVED IN: ")
print (Fore.WHITE + "%s/RawData/%s" % (PWD_salida, DOMINIO))

MKDIR_comando = "mkdir /usr/share/ID-entify/RawData"
MKDIR_resultado = subprocess.Popen(MKDIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

MKDIR_comando = ("mkdir /usr/share/ID-entify/RawData/%s" % (DOMINIO))
MKDIR_resultado = subprocess.Popen(MKDIR_comando, shell=True, stdout=subprocess.PIPE)
for MKDIR_salida in MKDIR_resultado.stdout:
 print(MKDIR_salida.decode(sys.getdefaultencoding()).rstrip())

time.sleep(5)

#print (Fore.RED + "\nEJECUTANDO:\n")
#print (Fore.YELLOW + "\nCreando diccionario de palabras relacionadas a %s \n" % (DOMINIO))

#DNSMAP_comand = ("cewl -w %s/RawData/%s_CEWL_Diccionario.txt -m 5 http://%s/" % (PWD_salida, DOMINIO, PAGINA_WEB))
#print (Fore.WHITE + (DNSMAP_comand))
#DNSMAP_proceso=subprocess.Popen(DNSMAP_comand, shell=True)
#for num in range(1):
#    print (Fore.WHITE + "Ejecutando CEWL en segundo plano")

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


DNSMAP_comand = ("dnsmap %s >> %s/RawData/%s/%s_DNSMAP.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO))
print (Fore.WHITE + (DNSMAP_comand))
DNSMAP_proceso=subprocess.Popen(DNSMAP_comand, shell=True)
for num in range(1):
    print (Fore.WHITE + "Running DNSMAP in the background")

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
BLINDCRAWL_comando = "perl /usr/share/Programs/blindcrawl.pl -d %s >> %s/RawData/%s/%s_BLINDCRAWL.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
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

print (Fore.YELLOW + "\nVerifying WAF\n")

COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "Completed %s de %s" % (COMPLETADO, TOTAL))
WHOIS_comando = "whois %s >> %s/RawData/%s/%s_WHOIS.txt" % (DOMINIO, PWD_salida, DOMINIO, DOMINIO)
print (Fore.WHITE + (WHOIS_comando))
WHOIS_resultado = subprocess.Popen(WHOIS_comando, shell=True, stdout=subprocess.PIPE)
for WHOIS_salida in WHOIS_resultado.stdout:
 print(WHOIS_salida.decode(sys.getdefaultencoding()).rstrip())
 
COMPLETADO = COMPLETADO + 1
print (Fore.GREEN + "COMPLETED SCRIPT %s de %s" % (COMPLETADO, TOTAL))

