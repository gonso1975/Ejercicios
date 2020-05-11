import json
import requests
import sys
from tabulate import *
import xml.dom.minidom
from ncclient import manager

def request_interface():
    requests.packages.urllib3.disable_warnings()


    url1 = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/"
    url2 = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces-state/interface"


    headers={"Accept":"application/yang-data+json",
             "Content-type":"application/yang-data+json"}

    basic_auth = ("cisco", "cisco123!")

    resp=requests.get(url1,headers=headers,auth=basic_auth,verify=False)
    resp2=requests.get(url2,headers=headers,auth=basic_auth,verify=False)


    if resp.status_code == 200 and resp2.status_code == 200:
        
        response_json = resp.json()
        response2_json = resp2.json()
        
        Interfaces_list = []

        for interface in response_json["ietf-interfaces:interfaces"]["interface"]:
            
            Interface_name = interface["name"]
            try:
                interface_IP = interface["ietf-ip:ipv4"]["address"][0]["ip"]
            except:
                interface_IP = "No IP assigned"
            
            for i in response2_json["ietf-interfaces:interface"]:
                if i["name"] == Interface_name:
                    interface_MAC = i["phys-address"]
                    break
            interfaces_details=[Interface_name, interface_IP, interface_MAC]               
            Interfaces_list.append(interfaces_details)
            
        table_header = ["Interface", "IP", "MAC"]
        print(tabulate(Interfaces_list, table_header))

    else:

        print("Upps .... something has gone wrong")
    

def create_interface():

    con = manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

    # Se ha intentado usar la plantilla que se utilizó en las practicas, abriendo desde un archivo xml tipo open("config-temp-ietf-interfaces.xml").read(), dando fallo

    yang_model_scheme = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{name}</name>
                <description>{description}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                    ianaift:softwareLoopback
                </type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{ip_address}</ip>
                        <netmask>{mask}</netmask>
                    </address>
                </ipv4>
            </interface>
         </interfaces>
    </config>"""


    interface_request = {}
    interface_request["name"] = "Loopback" + input("Put the new interface loopback number: ")
    interface_request["description"] = input("Description: ")
    interface_request["ip_address"] = input("Ip Address: ")
    interface_request["mask"] = input("Mask: ")

    netconf_data = yang_model_scheme.format(
        name=interface_request["name"],
        description=interface_request["description"],
        ip_address=interface_request["ip_address"],
        mask=interface_request["mask"]
        )

    netconf_reply = con.edit_config(target = 'running', config=netconf_data)

    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def delete_interface():

    con = manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

    yang_model_scheme= """
     <config>
         <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
             <interface operation="delete">
                 <name>{name}</name>
             </interface>
         </interfaces>
     </config>"""


    interface_delete = {}
    interface_delete["name"] = "Loopback" + input("Select Loopback number for delete ")


    netconf_data = yang_model_scheme.format(
            name = interface_delete["name"])


    netconf_reply = con.edit_config(target = 'running', config=netconf_data)

    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def routing_table():

    requests.packages.urllib3.disable_warnings()
    url = "https://192.168.56.101/restconf/data/ietf-routing:routing-state"

    headers = {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"
        }
    basic_auth = ("cisco","cisco123!")

    resp = requests.get(url, auth=basic_auth, headers=headers, verify=False)
    resp_json = resp.json()

    routes = []
    counter = 0
    for item in resp_json['ietf-routing:routing-state']['routing-instance'][0]['ribs']['rib'][0]['routes']['route']:
        counter +=1
        route = [
                counter,
                item['destination-prefix'],
                item['next-hop']['outgoing-interface']
            ]
        routes.append(route)

    tableHeader= ["ID","Destination network","Outgoing interface"]
    print(tabulate(routes,tableHeader))

def yang_model_1():

    requests.packages.urllib3.disable_warnings()
    api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    basicAuth = ("cisco","cisco123!")

    resp = requests.get(api_url, auth=basicAuth, headers=headers, verify=False)

    response_json = resp.json()

    print(json.dumps(response_json, indent=4))

def yang_model_2():

    requests.packages.urllib3.disable_warnings()
    api_url = "https://192.168.56.101/restconf/data/ietf-restconf-monitoring:restconf-state"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    basicAuth = ("cisco","cisco123!")

    resp = requests.get(api_url, auth=basicAuth, headers=headers, verify=False)

    response_json = resp.json()

    print(json.dumps(response_json, indent=4))
