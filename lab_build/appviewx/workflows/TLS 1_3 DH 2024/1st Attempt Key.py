import subprocess
import os
import json
import time
import datetime
import requests
import SSH_Helper

curvesList ='<%curvesList%>'

keynames = []

now = datetime.datetime.now()
timeToday = int(now.replace(minute=0, second=0, microsecond=0).timestamp())

endTime = timeToday + (60 * 60)
curves = []

for curve in curvesList:
    
    indexTime = str(int(timeToday) + int(curvesList.index(curve)))
    
    curveEach = curve + "-iu" + str(timeToday) + "-eu" + str(endTime)
    curves.append(curveEach)
    
    if curve not in ["x25519","x448"]:
        cmd1 = "openssl ecparam -name " +  curve + " -genkey -noout -out " + curveEach + ".pem"
        status, output = subprocess.getstatusoutput(cmd1)
        AVX::LOG(cmd1)
    else:
        cmd1 = "openssl genpkey -algorithm " + curve + " -out " + curveEach + ".pem"
        status, output = subprocess.getstatusoutput(cmd1)
        AVX::LOG(cmd1)        
    keyname = curveEach + '.pem'
    keynames.append(keyname)
    
gateway_base_url, gateway_key = SSH_Helper.fetch_gateway_properties()
serverName = "<%serverName%>".split(",")
session_id = "<%sessionId%>"
hsm_ip = "<%hsm_ip%>"
hsm_username = "<%hsm_username%>"
hsm_password = "<%hsm_password%>"

for each in serverName:

    device_ip = SSH_Helper.execute_query_explorer(session_id, gateway_base_url, gateway_key, "TLS - Fetch IP Address", hook_input = {"serverName":each})[0]["ip"]
    
    url = gateway_base_url + "avxapi/{}?gwkey=" + gateway_key + "&gwsource=external"
    url=url.format("platform-fetch-credentials")
    
    payload = {
        "payload": {
            "credentialName": each, 
            "source": "AppViewX"
        }
    }
    
    headers = {
      'Content-Type': 'application/json',
      'sessionId': '<%sessionId%>'
    }
            "credentialName": each, 
            "source": "AppViewX"
        }
    }
    
    headers = {
      'Content-Type': 'application/json',
      'sessionId': '<%sessionId%>'
    }
    
    response = requests.request("POST", url, headers=headers, data = json.dumps(payload),verify = False)
    res=json.loads(response.text)
    identity_key = res["response"]["identityKey"]
    userName = res["response"]["userName"]
    
    file_name = "id_key.pem"
    
    os.chmod(file_name, 0o777)
    
    with open(file_name, 'w') as file:
        file.write(identity_key)
        
    os.chmod(file_name, 0o400)
    
    cmd0 = "ssh -o StrictHostKeyChecking=no -i " + file_name + " " + userName + "@" + device_ip + " 'umask 022'"
    AVX::LOG(cmd0)
    status, output = subprocess.getstatusoutput(cmd0)
    AVX::LOG(output)
    
    cmd1 = "scp -o StrictHostKeyChecking=no -i " + file_name + " " + keynames[0] + " " + keynames[1] + " "+ keynames[2] + " " + userName + "@" + device_ip + ":/keys"
    AVX::LOG(cmd1)
    status, output = subprocess.getstatusoutput(cmd1)
    AVX::LOG(status)
    AVX::LOG(output)
    
    cmd2 = "/appviewx/dependencies/vw/dependencies/sshpass -p " + hsm_password + " /appviewx/dependencies/vw/dependencies/rsync -av -e 'ssh -o StrictHostKeyChecking=no' --rsync-path='sudo rsync' " + keynames[0] + " " + keynames[1] + " "+ keynames[2] + " " + hsm_username + "@" + hsm_ip + ":"
    AVX::LOG(cmd2)
    status, output = subprocess.getstatusoutput(cmd2)
    AVX::LOG(output)
    
AVX::OUTPUT({'keynames':keynames,'indexTime':indexTime,'curves':curves})