import sys
import os
import json
import time
import datetime
import paramiko
from logger_util import get_logger
logger = get_logger('TLS Connection Config')

port = 22
hsm_ip = "<%hsm_ip%>"
hsm_username = "<%hsm_username%>"
hsm_password = "<%hsm_password%>"

cmd = "<%cmd%>"
curves ='<%currentCurves%>'
device_name = "<%hsmServer%>"

indexTime = "<%indexTime%>" 

if __name__ == "__main__":
    try:
        count = 0
        for each in curves:
            indexTime = "<%indexTime%>" 
            indexTime = str(indexTime) + str(count)
            cmd.append("sudo pkcs11-tool --module=" + "/" + "usr" + "/" + "lib" + "/" + "softhsm" + "/" + "libsofthsm2.so -l --pin 12345678 --token netscout --write-object " + "/home/appviewx/" +  each + ".pem --type privkey --id " + indexTime + " --label " + each + " --usage-derive --extractable --login-type user")
            count = count + 1
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hsm_ip, port, hsm_username, hsm_password)
        for command in cmd:
            AVX::LOG(command)
            stdin, stdout, stderr = ssh_client.exec_command(command)
            AVX::LOG(stdout.read().decode())
            AVX::LOG(stderr.read().decode())
        ssh_client.close()
    
    except Exception as e:
        AVX::LOG('Error: ' + str(e))
    AVX::OUTPUT({ 'cmd':cmd})