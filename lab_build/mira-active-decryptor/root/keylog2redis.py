#!/usr/bin/env python3

import sys
import os
import datetime
import time
import json
import redis

# XXX TODO support multiple segments / directories and non-VM case
keylogdir = "/secure_disk/data/logs/nse/main0/keylog/"

# XXX TODO support SSL connection to REDIS
#redis_host = "127.0.0.1"
#redis_conn  = redis.Redis(host=redis_host, port=6379, db=0)
redis_host = "192.168.10.150"
redis_cacert = "/home/mira/certs/DigiCertCA.pem"
redis_conn  = redis.Redis(host=redis_host, port=6379, db=0,
                         ssl=True, ssl_cert_reqs="none")
#                         ssl=True, ssl_ca_certs=redis_cacert)

keylog2fastkey = {
    "CLIENT_HANDSHAKE_TRAFFIC_SECRET": "CHTS",
    "SERVER_HANDSHAKE_TRAFFIC_SECRET": "SHTS",
    "CLIENT_TRAFFIC_SECRET_0": "CTS0",
    "SERVER_TRAFFIC_SECRET_0": "STS0",
    "EXPORTER_SECRET": "XS",
    "CLIENT_RANDOM": "MK",
}

sent = {}

def save_json(j):
    # Only save well formed entries (XS is optional for now)
    if ("CR" in j and
        ("MK" in j or
         ("CHTS" in j and "SHTS" in j and "CTS0" in j and "STS0" in j))):

        # Fill in TLS version and display on console
        j["Type"] = "1.2" if "MK" in j else "1.3"
        print(repr(j))

        # Add to REDIS
        xadd_fields = { "fkj" : json.dumps(j) }
        redis_conn.xadd(name = "sk-cr" + j["CR"], fields = xadd_fields)

# Loop forever processing keylog files
while True:
    time.sleep(5)
    fns = os.listdir(keylogdir)
    fns.sort()
    for fn in fns:
        # Skip file if still being written to
        rc = os.system("/usr/sbin/fuser -s "+keylogdir+"/"+fn)
        if rc == 0: continue

        # Process file
        with open(keylogdir+"/"+fn) as f:
            j = {}
            for l in f.readlines():
                if not l.endswith("\n"): break
                v = l.upper().split()
                if len(v) != 3: break
                if v[0] == "UTCTIME":
                    if len(j) > 0: save_json(j)
                    j = {}
                    j["CR"] = v[1].lower()
                    j["X-Origin"] = "eto-middlebox"
                    try:
                        j["LastUsed"] =  datetime.datetime.utcfromtimestamp(int(float(v[2]))).isoformat() + "Z"
                    except:
                        pass
                fkk = keylog2fastkey.get(v[0], None)
                if fkk is not None: j[fkk] = v[2].lower()
        if len(j) > 1: save_json(j)

        # Remove file
        try:
            os.remove(keylogdir+"/"+fn)
        except:
            pass
