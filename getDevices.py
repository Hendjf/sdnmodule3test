"""
Script that logs into Cisco DNA Center always on sandbox
and retrieves a list of network devices

"""

#import requests library and basic HTTP auth to pass a username and password

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import getpass

#Defines global variables we don't want changed

#USER = "devnetuser"
USER = input("Please Enter Your Username: ")
#PASS = "Cisco123!"
PASS = getpass.getpass()
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"


#Create dictionary for the resposne payload, headers, in this we are doing an http post
#so we need to specify the content type we are sending rather than accepting a format

headers = {'Content-Type': 'application/json'}

#creates a response variable with the value of our post request notice this is a post not a get
#which is different than what we have been doing so far we are sending the server something not
#asking for it.  Also note we are passing a username and password and lastly as you will notice
#in the next lab we have set verify to false this is because DNA Center is using a self signed
#certificate and we are aware so we want to accept the risk and continue
#THIS SHOULD NOT BE DONE IN A PRODUCTION ENVIRONMENT IT IS A SECURITY ISSUE!!!!

response = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

#converts our respone to json format and stores it in our variable resposneJSON

token = response.json()['Token']

#prints responseJSON variable

#print("Your generated token is: " + token)

#Creates a variable URL2 and assigns the value of the follow up API request
#to DNA Center to retrieve a list of network devices

#URL2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

URL2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/interface"

#Creates dictionary for follow up get request headers specifying the format as JSON and
#passing the value for the token from the variable above.

getHeader = {'Accept': 'application/json', 'X-auth-token': token}

#Creates object getResponse with the contents of our http get request to the URL2 variable
#passing our getHeader dictionary and not verifying the cert validity since it is self signed 

getResponse = requests.get(URL2, headers=getHeader, verify=False)

#Takes our response variable and converts it to JSON format storing it in devicesJSON

#devicesJSON = getResponse.json()
interfacesJSON = getResponse.json()

#devices =getResponse.json()['response']
#for device in devices:
	#name = device['hostname']
	#mgmtIP = device['managementIpAddress']
	#print("The Device Named: " + str(name) + " is at IP " + str(mgmtIP))
 
#interfaces = getResponse.json()['response']
#for interface in interfaces:
	#interface = interfacesJSON['response']
	#hamburgers = interface['id']
	#ketchup = interface['adminStatus']
#device = devicesJSON['response']
#deviceName = device['hostname']
#deviceIP = device['managementIpAddress']

#print("ID is " + str(hamburgers) + " is administravtively " + str(ketchup))
#print("Device Named " + deviceName + "is at IP " + deviceIP)

#prints devicesJSON to the screen

#pprint(devicesJSON)
Hamburgers ="10.0.1.0"
Ketchup= "Toppings"

pprint(interfacesJSON)

print(Hamburgers)
print(Ketchup)
