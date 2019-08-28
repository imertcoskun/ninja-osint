import subprocess
import os
import nmap
import whois
import json


girdi = raw_input("bir arguman gir la....")
# def nmap_tarama():
#     nm = nmap.PortScanner()
#     nm.scan(girdi,'21,22,23,25,53,67,68,80,143,443,','-sS -sV -Pn -O')
#     nm.scaninfo()
#     nm.csv()
#     print nm.csv()

#     nmap_veriler = {
#     "Taratilan_Host_Adi" : girdi,
#     "host_scanned_port" : "21,22,23,25,53,67,68,143,443",
#     "host_argument" : "-sS -sV -Pn -O"
#     "Tarama_Sonucu" : nm.csv
     
#     }
#     with open ('json.txt','w') as outfile:
#         json.dump(nmap_veriler,outfile)

# nmap_tarama()

# def nmap_tarama():
#     print "nmap taramasi basliyor..."
#     nm = nmap.PortScanner()
#     nm.scan(girdi,'21,22,23,25,53,67,68,80,143,443,','-sS -sV -Pn -O')
#     nm.scaninfo()
#     nm.csv()
#     print nm.csv()

#     nmap_veriler = {
#             "Taratilan_Host_Adi" : girdi,
#             "host_scanned_port" : "21,22,23,25,53,67,68,143,443\n",
#             "host_argument" : "-sS -sV -Pn -O\n",
#             "Tarama_Sonucu" : nm.csv()
#     }
#     with open ('json.txt','w') as outfile:
#             json.dump(nmap_veriler,outfile)

import logging

# extra modules
dependencies_missing = False
try:
    import requests
except ImportError:
    dependencies_missing = True

from metasploit import module


metadata = {
    'name': 'Python Module Example',
    'description': '''
        Python communication with msfconsole.
    ''',
    'authors': [
        'Jacob Robles'
    ],
    'date': '2018-03-22',
    'license': 'MSF_LICENSE',
    'references': [
        {'type': 'url', 'ref': 'https://blog.rapid7.com/2017/12/28/regifting-python-in-metasploit/'},
        {'type': 'aka', 'ref': 'Coldstone'}
    ],
    'type': 'single_scanner',
    'options': {
        'targeturi': {'type': 'string', 'description': 'The base path', 'required': True, 'default': '/'},
        'rhost': {'type': 'address', 'description': 'Target address', 'required': True, 'default': None}
    }
}



def run(args):
    module.LogHandler.setup(msg_prefix='{} - '.format(args['rhost']))
    if dependencies_missing:
        logging.error('Module dependency (requests) is missing, cannot continue')
        return

    # Your code here
    try:
        r = requests.get('https://{}/{}'.format(args['rhost'], args['targeturi']), verify=False)
    except requests.exceptions.RequestException as e:
        logging.error('{}'.format(e))
        return

    logging.info('{}...'.format(r.text[0:50]))


if __name__ == '__main__':
    module.run(metadata, run)














# import shodan
# SHODAN_API_KEY = "4uXvxzSWh9vOTKrv7jEb0Qt1EA8mwVrx"
# api = shodan.Shodan(SHODAN_API_KEY)
# host_ismi = raw_input("host bilgisi girin...")
# host = api.host(host_ismi)

# # Print general info
# print("""
#         IP: {}
#         Organization: {}
#         Operating System: {}
# """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

# # Print all banners
# for item in host['data']:
#         print("""
#                 Port: {}
#                 Banner: {}
#         """.format(item['port'], item['data']))




# import shodan 
# import sys ,requests , smtplib, json
# API_KEY = "4uXvxzSWh9vOTKrv7jEb0Qt1EA8mwVrx"
# api = shodan.Shodan(API_KEY)
# def taramashodan():
#         target = raw_input("Enter the address :")
#         ask = "https://api.shodan.io/dns/resolve?hostnames=" + target + "&key=" + API_KEY
#         response = requests.get(ask)
#         get_json = json.loads(response.text)
#         ip_addr = get_json[target]
        
#         host = api.host(ip_addr)
#         open_ports = []
#         for i in host["data"]:
#             open_ports.append(i["port"])