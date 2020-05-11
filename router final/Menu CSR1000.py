import json
import requests
from tabulate import *
from CSR_functions import *

print("######################################################################")
print("In this menu you can select the next options for CSR1000v")
print("1 - Get Interfaces list")
print("2 - Create interfaces")
print("3 - Delete interfaces")
print("4 - Get Routing Table")
print("5 - Get Yang Model ietf-interfaces:interfaces")
print("6 - Get Yang Model ietf-restconf-monitoring:restconf-state")
print("Select 'q' or'quit' for exit")
print("#######################################################################")

while True:
    input_user = input("Selet your option ")
    if input_user == "quit" or input_user == "q":
        break
    if input_user == "1":
        request_interface()
        break
    if input_user == "2":
        create_interface()
        break
    if input_user == "3":
        delete_interface()
        break
    if input_user == "4":
        routing_table()
        break
    if input_user == "5":
        yang_model_1()
        break
    if input_user == "6":
        yang_model_2()
        break
