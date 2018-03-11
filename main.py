import time, os
from pynput.keyboard import Key, Controller
import mkj_pkg.main as mkj

keyboard = Controller()
os.system("clear")

mkj.important(" This script performs a DIRB & NMAP scan on the desired / URL ")
time.sleep(1)
os.system("clear")
mkj.important(" Please make sure to add http / https in your URL.")
time.sleep(1)
os.system("clear")

print("What is your desired URL? ")
lastIP = open("lastIP.txt", "w")
ipURL = raw_input("")
lastIP.write(ipURL)
lastIP.close()
os.system("clear")

print("What sleep offset would you like to use?")
offset = raw_input()
os.system("clear")

os.system("gnome-terminal")
time.sleep(1)
mkj.ty("python secondary.py")
mkj.pr(Key.enter)
os.system("dirb " + ipURL)
time.sleep(offset)

#os.system("gnome-terminal")
#os.system("nmap -sV -Pn " + ipURL)
