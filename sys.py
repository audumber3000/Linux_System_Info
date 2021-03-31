import socket
import json
import os
import base64
import sys
import speedtest
import requests
import platform
from termcolor import colored
# from urllib2 import urlopen
from urllib.request import urlopen


def network ():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print("User :" + hostname)    
    

    def is_connected():
       try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
       except OSError:
        pass
       return False

    if(is_connected()==True):
        print(colored('Internet connection OK' , 'green' , attrs=['bold' , 'reverse', 'blink']))

        
        s = speedtest.Speedtest()
        

        print(colored(f'Upload Speed : {s.download(threads=None)/1e+6}' , "green"))
        print(colored(f'Download Speed : {s.upload(threads=None)/1e+6}' , "green"))
        
        
      #   Url = "https://geo.ipify.org/api/v1?apiKey=at_yxxDWNsLvdqKjrPHbiufYWJT2x1FA=8.8.8.8"
      #   r = requests.get(url = Url)
      #   print(r.json())

        from requests import get

        ip1 = get('https://api.ipify.org').text
        print(colored('Public IP : {}'.format(ip1) , "green"))

        ip = ip1
        api_key = 'at_yxxDWNsLvdqKjrPHbiufYWJT2x1FA'
        api_url = 'https://geo.ipify.org/api/v1?'

        url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip
        data = urlopen(url).read().decode('utf8')
        final_data = json.loads(data)
        z = final_data["location"]
        y = final_data["as"]
        x = final_data["proxy"]
       
        print(colored(f'Country : {z["country"]} ' , "green" ))
        print(colored(f'Region : {z["region"]} ' , "green" ))
        print(colored(f'Region : {z["lat"]} ' , "green"))
        print(colored(f'Latitu : {z["lng"]} ' , "green"))
        print(colored(f'timezone : {z["timezone"]} ' , "green"))
        
        print(colored(f'Network : {y["name"]} ' , "green"))
        print(colored(f'ISP : {final_data["isp"]} ' , "green"))

        if(x["proxy"]==False):

           print(colored(f'Proxy : {x["proxy"]} ' , "yellow"))
           print(colored(f'VPN : {x["vpn"]} ' , "yellow"))
           print(colored(f'TOR : {x["tor"]} ' , "yellow"))

        else:
           print(colored(f'Proxy : {x["proxy"]} ' , "green"))
           print(colored(f'VPN : {x["vpn"]} ' , "green"))
           print(colored(f'TOR : {x["tor"]} ' , "green"))

       
        
        
        

    else:
       print(colored('NO Internet connection :( ' , 'red' , attrs=['bold' , 'reverse', 'blink']))
       
       
def Battery_Health():
   
   charge_state = open("/sys/class/power_supply/BAT0/status" , "r").readline().strip()
   manufacturer = open("/sys/class/power_supply/BAT0/manufacturer" , "r").readline().strip()

   capacity = open("/sys/class/power_supply/BAT0/capacity" , "r").readline().strip()

   current_now = open("/sys/class/power_supply/BAT0/current_now" , "r").readline().strip()

   model_name = open("/sys/class/power_supply/BAT0/model_name" , "r").readline().strip()

   technology = open("/sys/class/power_supply/BAT0/technology" , "r").readline().strip()

   serial_number = open("/sys/class/power_supply/BAT0/serial_number" , "r").readline().strip()
   ty = open("/sys/class/power_supply/BAT0/type" , "r").readline().strip()
   charge_full = open("/sys/class/power_supply/BAT0/charge_full" , "r").readline().strip()
   charge_full_design = open("/sys/class/power_supply/BAT0/charge_full_design" , "r").readline().strip()

   print(f'Model Name : {model_name}')
   print(f'Manufacturer Name : {manufacturer}')
   print(f'Serial Number : {serial_number}')
   print(f'Capacity : {capacity}')
   print(f'Charge Status : {charge_state}')
   print(f'Current Now : {current_now}')
   print(f'Battery Type : {ty}')
   
   print(f'Charge full Design: {charge_full_design}')
   print(f'Charge full : {charge_full}')
   

   


def System_info():
    
# Architecture
     print("Architecture: " + platform.architecture()[0])

# machine
     print("Machine: " + platform.machine())

# node
     print("Node: " + platform.node())

# system
     print("System: " + platform.system())


   





def email():
   
   port = 465  # For SSL
   password = input("Type your password and press enter: ")

   # Create a secure SSL context
   context = ssl.create_default_context()


   sender_email = "vishal@gmail.com"
   receiver_email = "audumberchaudhari1003@gmail.com"
   message = """\
   Subject: Hi there

   This message is sent from Python."""



   for i in range(1,20):
      with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("audumberchaudhari3000@gmail.com", "Password")
            server.sendmail(sender_email, receiver_email, message)
            print(f'Email sent {i}')



network()
Battery_Health()
System_info()