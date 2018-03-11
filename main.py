import time, os
from pynput.keyboard import Key, Controller
import mkj_pkg.main as mkj

keyboard = Controller()
os.system("clear")

mkj.important(" This script performs a DIRB & NMAP scan on the desired IP / URL ")
time.sleep(2)
os.system("clear")
mkj.important(" Please make sure to add http / https if you chose to use a URL ")
time.sleep(2)
os.system("clear")

print("What is your desired URL / IP? ")
ipURL = input("")
os.system("clear")

print("What sleep offset would you like to use?")
offset = input()
os.system("clear")

os.system("dirb " + ipURL)
time.sleep(offset)

os.system("gnome-terminal")
os.system("nmap -sV -Pn " + ipURL)