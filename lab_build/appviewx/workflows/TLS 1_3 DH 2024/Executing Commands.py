import sys
import os
import json
import time
import datetime
import subprocess
from logger_util import get_logger
logger = get_logger('TLS Connection Config')

curves ='<%currentCurves%>'

if __name__ == "__main__":
    try:
        cmd = []
        # Specify the path to your environment variables file
        env_file_path = 'akp.env'
        
        # Read the file and set environment variables
        with open(env_file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                os.environ[key] = value

        for each in curves:
            cmd1 = "/appviewx/dependencies/appviewx_addons/Python/bin/python final.py -k " + each + ".pem -d " + each + ".der"
            cmd.append(cmd1)
            cmd2 = "/appviewx/dependencies/appviewx_addons/Python/bin/python add_external_key.py -n -s https://$AKP_SERVER/api -t $AKP_TOKEN -u $AKP_UUID -d " + each + ".der"
            cmd.append(cmd2)
            cmd3 = "rm -rf " + each + ".pem " + each + ".der"
            cmd.append(cmd3)
        AVX::LOG(cmd)
        
        for command in cmd:
            AVX::LOG(command)
            result = subprocess.run(command, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                AVX::LOG("Command output:")
                AVX::LOG(result.stdout)
            else:
                AVX::LOG("Command failed with exit code:", result.returncode)
                AVX::LOG("Error output:")
                AVX::LOG(result.stderr)
    
    except Exception as e:
        AVX::LOG('Error: ' + str(e))
    AVX::OUTPUT({ 'cmd':cmd})