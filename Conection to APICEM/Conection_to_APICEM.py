import json
import requests
from tabulate import *
from my_apic_em_functions import *

print("######################################################################")
print("In this menu you can select the next options in the APIC-EM")
print("1 - Get Hosts list of network devices filtered by hostType and hostIp")
print("2 - Get the list of network devices filtered by Family , Type and MAC")
print("3 - Get the list of reachable devices")
print("4 - Get the IP Pool available")
print(" Select 'q' or'quit' for exit")
print("#######################################################################")

while True:
    input_user = input("Selet your option ")
    if input_user == "quit" or input_user == "q":
        break
    if input_user == "1":
        print_hosts()
    if input_user == "2":
        print_devices()
    if input_user == "3":
        get_reachable_dev()
    if input_user == "4":
        get_ippool()
