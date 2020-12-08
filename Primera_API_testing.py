import requests
from requests.auth import HTTPBasicAuth
import json
username="3paradm"
password="3pardata"
def getSessionKey():
	headers = {'Content-type': 'application/json','Accept': 'application/json'}
	data={'user':'3paradm','password':'3pardata'}
	data=json.dumps(data)
	response = requests.post(url="https://IP_Storage/api/v1/credentials",headers=headers,data=data,verify=False)
	result=response.json()['key']
	return result

def getVolumes(key):
	print("Key: "+key)
	headers = {'Content-type': 'application/json','Accept': 'application/json','X-HP3PAR-WSAPI-SessionKey':key,\
	'charset':'UTF-8','user':'3paradm','password':'3pardata'}
	response = requests.get("https://IP_Storage/api/v1/volumes",headers=headers,auth = HTTPBasicAuth(username, password),verify=False)
	list_vol=[]
	for i in response.json()['members']:
		#print(i)
		a_vol={}
		a_vol['name']=i['name']
		a_vol['size']=i['sizeMiB']
		a_vol['usage']=i['adminSpace']['usedMiB']
		list_vol.append(a_vol)
	for a_vol in list_vol:
		print("Name: {0} - Size: {1} MB - Usage: {2} MB".format(a_vol['name'],a_vol['size'],a_vol['usage']))


def createLUN(key,name,size,cpg):
	headers = {'Content-type': 'application/json','Accept': 'application/json','X-HP3PAR-WSAPI-SessionKey':key,\
	'charset':'UTF-8','user':'3paradm','password':'3pardata'}
	data={'name':name,'sizeMiB':size,'cpg':cpg,'tpvv':True}
	data=json.dumps(data)
	response = requests.post(url="https://IP_Storage/api/v1/volumes",headers=headers,data=data,verify=False)
	print(response.json())


key=getSessionKey()
getVolumes(key)
print("-------------------------------------------")
createLUN(key,'VOLUME-TEST06',30000,'SSD_r6')
print("-------------------------------------------")
getVolumes(key)
