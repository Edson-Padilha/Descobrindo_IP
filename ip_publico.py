import requests
from time import sleep

ip_publico = requests.get('https://api.ipify.org/').text
sleep(4)
print('----------------------------')
print(f'IP Publico: {ip_publico}')
print('----------------------------')

import socket

ip_local = socket.gethostbyname(socket.gethostname())
print('----------------------------')
print(f'IP Local: {ip_local}')
print('----------------------------')

#189.45.201.243