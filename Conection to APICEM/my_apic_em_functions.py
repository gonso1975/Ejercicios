import json       # Import JSON encoder and decoder module
import requests   # requests module used to send REST requests to API

from tabulate import *

    
def get_ticket():

    requests.packages.urllib3.disable_warnings()  

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket" 


    headers = {
        "content-type": "application/json"
    }

    body_json = {
      "username": "devnetuser",
      "password": "Xj3BDqbU"
    }

    resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)

    print("Ticket request status: ", resp.status_code)
    
    response_json = resp.json()

    serviceTicket = response_json["response"]["serviceTicket"]

    #print("The service ticket number is: ", serviceTicket)

    return serviceTicket

def print_hosts():
    
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"

    ticket = get_ticket()

    headers = {
        "content-type": "application/json",
        "x-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    #print("Status of Host request:", resp.status_code)

    response_json = resp.json()

    host_list = []
    i = 0

    for item in response_json ["response"]:
        i+=1
        host = [
                i,
                item["hostType"],
                item["hostIp"]
                ]
        host_list.append(host)

    table_header = ["Number","Type","IP"]

    print( tabulate(host_list,table_header))

def print_devices():

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"

    ticket = get_ticket()

    headers = {
        "content-type": "application/json",
        "x-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    print("Status of Host request:", resp.status_code)

    response_json = resp.json()

    devices_list = []
    i = 0

    for item in response_json ["response"]:
        i+=1
        host = [
                i,
                item["family"],
                item["type"],
                item["macAddress"]
                ]
        devices_list.append(host)

    table_header = ["Number","Family","Type","MAC"]

    print( tabulate(devices_list,table_header))

def get_ippool():
    
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ippool"

    ticket = get_ticket()

    headers = {
        "content-type": "application/json",
        "x-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    print("Status of Host request:", resp.status_code)

    response_json = resp.json()

    host_list = []
    i = 0

    for item in response_json["response"]:
        i += 1
        host = [
            i,
            item["ipPool"]
        ]
        host_list.append(host)

    table_header = ["Number", "ipPool"]

    print(tabulate(host_list, table_header))

def get_reachable_dev():

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/reachability-info"

    ticket = get_ticket()

    headers = {
        "content-type": "application/json",
        "x-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    print("Status of Host request:", resp.status_code)

    response_json = resp.json()

    #pprint(response_json)

    host_list = []
    i = 0

    for item in response_json["response"]:
        i += 1
        host = [
            i,
            item["discoveryId"],
            item["mgmtIp"]
        ]
        host_list.append(host)

    table_header = ["Number", "Type", "IP"]

    print(tabulate(host_list, table_header))

