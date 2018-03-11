import os, time, socket

lastIP = open("lastIP.txt", "r")
ip = lastIP.read()
print (ip)
final = socket.gethostbyname(ip)
os.system("nmap -sV -Pn " + final)
lastIP.close()

